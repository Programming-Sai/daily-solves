def canCompleteCircuit(gas, cost) -> int:
    gas_total, cost_total, start, current_gas_tank = 0, 0, 0, 0
    for i in range(len(gas)):
        current_gas_tank += (gas[i] - cost[i])
        gas_total += gas[i]
        cost_total += cost[i]
        if current_gas_tank < 0:
            current_gas_tank, start = 0, i + 1
    if gas_total >= cost_total: return start
    else: return -1