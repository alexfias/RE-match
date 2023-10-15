import pandas as pd

def compute_node_resilience_metrics(network, snapshots=None):
    """
    Compute the resilience and reliability metrics for each node in the network.

    Returns:
    - dict: Dictionary where the key is the node and the value is another dictionary
            containing the computed metrics for that node.
    """

    node_metrics = {}

    for bus in network.buses.index:
        # Extract the load and generation time series for the current bus
        demand = network.loads_t.p_set[bus] if bus in network.loads_t.p_set.columns else 0
        generation = network.generators_t.p[bus] if bus in network.generators_t.p.columns else 0
        
        unserved_energy = (demand - generation).clip(lower=0)
        lolp = (unserved_energy > 0).mean()
        eens = unserved_energy.mean()

        node_metrics[bus] = {
            "LOLP": lolp,
            "EENS": eens
        }

    return node_metrics

def compute_weighted_network_resilience(network, snapshots=None):
    """
    Compute the weighted resilience and reliability metrics for the entire network,
    where each node's metrics are weighted by its average load.

    Returns:
    - dict: Dictionary containing the computed weighted metrics.
    """
    node_metrics = compute_node_resilience_metrics(network, snapshots)
    
    total_demand = network.loads_t.p_set.sum().sum()  # Total demand across all snapshots and buses
    weighted_lolp = 0
    weighted_eens = 0

    for bus, metrics in node_metrics.items():
        average_load = network.loads_t.p_set[bus].mean() if bus in network.loads_t.p_set.columns else 0
        weight = average_load / total_demand
        weighted_lolp += weight * metrics["LOLP"]
        weighted_eens += weight * metrics["EENS"]

    return {
        "Weighted LOLP": weighted_lolp,
        "Weighted EENS": weighted_eens
    }
