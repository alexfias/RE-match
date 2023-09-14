import pypsa
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def compute_rmi(network_path):
    # Load the network
    network = pypsa.Network(network_path)

    # Calculate the mismatch (generation - load) at each node and each hour
    mismatch = network.generators_t.p.groupby(network.generators.bus, axis=1).sum() - network.loads_t.p_set.groupby(network.loads.bus, axis=1).sum()

    # Calculate the spatial correlation between nodes
    spatial_corr = mismatch.corr()

    # Calculate the temporal correlation between hours
    temporal_corr = mismatch.T.corr()

    # Normalize the correlations to range from 0 to 1
    scaler = MinMaxScaler()
    spatial_corr_normalized = scaler.fit_transform(spatial_corr)
    temporal_corr_normalized = scaler.fit_transform(temporal_corr)

    # Combine the spatial and temporal correlations to create the index
    index = (spatial_corr_normalized + temporal_corr_normalized) / 2

    # Calculate the overall index for the entire network
    overall_index = index.mean().mean()

    return overall_index
