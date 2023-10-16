import pypsa

def compute_economic_metrics(network: pypsa.Network):
    """Compute economic metrics to investigate the match between renewable generation and demand.

    Parameters:
    - network (pypsa.Network): The PyPSA network for which metrics should be computed.

    Returns:
    dict: A dictionary containing calculated economic metrics.
    """

    # 1. Marginal Cost of Generation for each generator
    marginal_costs = network.generators['marginal_cost']

    # 2. Total System Cost
    total_system_cost = sum(network.generators_t.p.multiply(network.generators['marginal_cost'], axis=1).sum())

    # 3. Value of Lost Load
    voll = 10000  # in $/MWh, adjust as per your requirements
    mismatch = network.loads_t.p_set - network.generators_t.p.sum(axis=1)
    lost_load_cost = (mismatch[mismatch > 0] * voll).sum()

    # 4. Backup Generation Cost
    backup_generation_cost = 50  # in $/MWh, adjust as per your requirements
    backup_cost = (mismatch[mismatch > 0] * backup_generation_cost).sum()

    # 6. Curtailment Costs
    curtailed_energy = network.generators_t.p_max_pu.multiply(network.generators['p_nom_opt']) - network.generators_t.p
    curtailment_cost = curtailed_energy[curtailed_energy > 0].multiply(network.generators['marginal_cost']).sum().sum()

    # Return as a dictionary
    metrics = {
        'Marginal Costs': marginal_costs,
        'Total System Cost': total_system_cost,
        'Value of Lost Load Cost': lost_load_cost,
        'Backup Cost': backup_cost,
        'Curtailment Cost': curtailment_cost
    }

    return metrics
