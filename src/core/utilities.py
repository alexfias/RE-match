import pypsa 

def calculate_mismatch(network, snapshots=None):
    """
    Calculate the mismatch (Demand - Generation) for every node in the network.
    
    Returns:
    - DataFrame: A DataFrame where each column represents a node and the rows are the mismatch values.
    """
    if snapshots is None:
        snapshots = network.snapshots
        
    demand = network.loads_t.p_set
    generation = network.generators_t.p.sum(axis=1)

    mismatch = demand.sub(generation, axis=0)
    
    return mismatch
