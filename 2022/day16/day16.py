'''
@author: BastienZim

'''

import os
import numpy as np
import itertools

path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
#path = "/home/bastien/Documents/AdventOfCode/2022"


example = True


def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()

    valves, flow, connections = sanitize_input(input)
    map = {v: c for v, c in zip(valves, connections)}
    # drop valves that have no flow)()
    distances, _ = Dijkstra(valves[0], valves[1], map)
#    print(distances)

    good_valves = [v for v, f in zip(valves, flow) if f > 0]
    # forget bad valves
    flow = {v: f for v, f in zip(valves, flow) if v in good_valves}

    distances, _ = Dijkstra(valves[0], valves[1], map)
    # INIT STATE
    # if(valves[0] not in good_valves):
    #    first_valve = good_valves[np.argmin(
    #        [distances[g] for g in good_valves])]
    #    init_time = 30 - min([distances[g] for g in good_valves])
    #    print(f"First valve is {first_valve}, starting time: {init_time} minutes")
    # else:
    first_valve = valves[0]
    init_time = 29
    init_total_flow = 0

    # DROP useless stuff
    good_distances = {v: {} for v in good_valves}
    good_distances[first_valve] = {}
    for i, v1 in enumerate(good_valves):
        good_distances[first_valve][v1] = distances[v1]
        good_distances[v1][first_valve] = distances[v1]
        good_distances[v1][v1] = 0
        for v2 in good_valves[i+1:]:
            distances, _ = Dijkstra(v1, v2, map)
            #if(distances[v2]>10):
            #    print("OMEGA BIG",distances[v2],v1, v2)
            good_distances[v1][v2] = distances[v2]
            good_distances[v2][v1] = distances[v2]

    closed_valves = good_valves.copy()

    




    # print(greedy(current_valve, closed_valves,
    #      init_total_flow, time, flow, good_distances))

    #best_order = ["DD","BB","JJ","HH","EE","CC"]
    #total_flow = run_order(best_order, first_valve, closed_valves, init_total_flow, init_time, flow, good_distances)

    #print(f"            FINAL RESULT ==> {total_flow} ==> best {best_order}")

    #Try everything...


#    current_best, best_perm = try_all_permuts(first_valve, closed_valves, init_total_flow, init_time, flow, good_distances)
#    print(current_best, best_perm)
    
    '''    order, total_flow = all_try(first_valve, good_valves,
                            init_total_flow, init_time, flow, good_distances)
        
        print(f"First RESULT ==> {total_flow} ==> order {order}")
        current_best = total_flow
        for i in range(len(order)):
            for j in range(i+1,len(order)):
                swap_order = order.copy()
                swap_order[i],swap_order[j] = swap_order[j],swap_order[i]
                #print(i,j)
                total_flow = run_order(swap_order, first_valve, closed_valves, init_total_flow, init_time, flow, good_distances)
                if(total_flow>current_best):
                    current_best = total_flow
                    print("==>",total_flow,swap_order)
                if(total_flow == 1651):
                    print("HERE")
                print(f"            FINAL RESULT ==> {total_flow} ==> order {swap_order}")
    '''

    print(good_distances)
    Dijkstra_adapt("AA", good_distances)


def try_all_permuts(first_valve, closed_valves, init_total_flow, init_time, flow, good_distances):
    """Too costly."""

    current_best = 0
    for perm in (itertools.permutations(closed_valves)):
        total_flow = run_order(perm, first_valve, closed_valves, init_total_flow, init_time, flow, good_distances)
        if(total_flow>current_best):
                current_best = total_flow
                best_perm = perm
                print(total_flow,perm)
    print(f"            FINAL RESULT ==> {current_best} ==> order {best_perm}")
    return(current_best, best_perm)

def run_order(order, current_valve, closed_valves, total_flow, time, flow, good_distances):
    i_chosen = 0
    while(time >= 0):
        #print(f" Time: {30-time},current_v {current_valve}, releasing {sum([flow[v] for v in flow.keys() if v not in closed_valves])} pressure")
        #print(f" total flow = {total_flow}")
        if(len(closed_valves) > 0):
            #print(len(order), i_chosen)
            chosen = order[i_chosen]
            i_chosen += 1
            if(i_chosen>len(order)):
                time = -1
                break
            #print(f"Chosen: {chosen}")
            current_valve, time, total_flow, closed_valves = update(
                chosen, current_valve, closed_valves, total_flow, time, flow, good_distances)
        else:
            time = -1
    #print("\n            FINAL RESULT ==>  ", total_flow, "J")
    return total_flow


def all_try(current_valve, closed_valves, total_flow, time, flow, good_distances):
    order = []
    while(time >= 0):
        if(len(closed_valves) > 0):
            candidates = get_candidates_f_d_gain(
                current_valve, closed_valves, time, flow, good_distances)
            if(len(candidates)==0):
                time =-1
                break
            filter_candidate(candidates, current_valve, closed_valves,
                             total_flow, time, flow, good_distances)
            chosen = candidates[0][0]
            order.append(chosen)
            current_valve, time, total_flow, closed_valves = update(
                chosen, current_valve, closed_valves, total_flow, time, flow, good_distances)
        else:
            time = -1
        #print(f"t:{30-time}, flow = {total_flow}, node= {current_valve}")
    #print(f"\n            FINAL RESULT ==> {total_flow} ==> order {order}")
    return order, total_flow


def filter_candidate(candidates, current_valve, closed_valves, total_flow, time, flow, good_distances):
    """ each candidate : v, f, d, flow_added """
    #print(candidates,len(candidates))
    if(len(candidates)<=1):
        return(candidates)
    filt_cand = sorted(candidates.copy(), key=lambda x: x[2])
    # for the same distance remove the less beneficial one
    for i, c1 in enumerate(filt_cand):
        for c2 in filt_cand[i+1:]:
            if(c1[2] == c2[2]):
                if(c1[3] < c2[3]):
                    filt_cand.remove(c1)
                    break
                else:
                    filt_cand.remove(c2)
    max_pot = 0
    best_cand = filt_cand[0]
    for c in filt_cand:
        new_valve, new_time, new_total_flow, new_closed_valves = update(
            c[0], current_valve, closed_valves, total_flow, time, flow, good_distances)
        potential_candidates = get_candidates_f_d_gain(
            new_valve, new_closed_valves, new_time, flow, good_distances)
        if(len(potential_candidates) > 0):
            node_potential = c[3] + max([x[3] for x in potential_candidates])
        else:
            node_potential = c[3]
        if(node_potential > max_pot):
            max_pot = node_potential
            best_cand = c

    return([best_cand])

def update(choice, current_valve, closed_valves, total_flow, time, flow, good_distances):
    #print(f"  UPDATE | time: {30-time}, opening: {choice}")

    closed_upd = closed_valves.copy()
    # print(good_distances["AA"],good_distances["DD"])
    time_upd = time - (good_distances[choice][current_valve] + 1)
    #print(f"  ---Activating choice: {choice}, flow: {flow[choice]}; Time:{30-time_upd} -> remaining {time_upd} min")
    total_flow_upd = total_flow + (time_upd+1) * flow[choice]
    closed_upd.remove(choice)

    #print(f"  aft UPDATE | time: {30-time_upd} d+1={good_distances[choice][current_valve] + 1}, from: {total_flow_upd}")
    return(choice, time_upd, total_flow_upd, closed_upd)


def get_candidates_f_d_gain(current_valve, closed_valves, time, flow, good_distances):
    candidates = []
    for v in closed_valves:
        f = flow[v]
        if(v != current_valve):
            d = good_distances[current_valve][v]
        else:
            d = 0
        if(time-d-1>0):
            candidates.append((v, f, d, (time-d-1)*f))

    return candidates
# def get_potential_flow(start, candidate, distances):


def eventual_press_release(t, f):
    return(t*f)


def Dijkstra(start, end, map):
    # [(i,j) for i in range(0,map_shape[0]) for j in range(0,map_shape[1])]
    nodes = map.keys()
    unvisited = {node: None for node in nodes}
    parents = {}
    distances = {}
    node = start
    current_distance = 0
    while(True):
        neighbours = map[node]  # (node, map, map_shape)
        # for dist neighbor in neighbours
        for dist, n in zip([1 for x in neighbours], neighbours):
            if(n not in unvisited):
                continue
            new_Distance = dist + current_distance
            if(unvisited[n] is None or new_Distance < unvisited[n]):
                unvisited[n] = new_Distance
                parents[n] = node

        distances[node] = current_distance
        del unvisited[node]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        node, current_distance = sorted(candidates, key=lambda x: x[1])[0]
    return(distances, parents)


def greedy(current_valve, closed_valves, total_flow, time, flow, good_distances):
    while(time >= 0):
        if(len(closed_valves) > 0):
            candidates = get_candidates_f_d_gain(
                current_valve, closed_valves, time, flow, good_distances)
            chosen = max(candidates, key=lambda x: x[3])[0]
            current_valve, time, total_flow, closed_valves = update(
                chosen, current_valve, closed_valves, total_flow, time, flow, good_distances)
    #
        else:
            time = -1
        #print(f"t:{30-time}, flow = {total_flow}, node= {current_valve}")
    return total_flow


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    input = list(map(lambda x: x.replace("\n", ""), input))
    valves, flow, connections = [], [], []
    for x in input:
        elts = x[6:].split(" has flow rate=")
        name, elts = elts[0], elts[1]
        elts = elts.split("; ")
        rate, elts = elts[0], elts[1]
        for x in ["tunnel leads to valve ", "tunnels lead to valves "]:
            if(x in elts):
                elts = elts.replace(x, "")
        connect = elts.split(", ")
        valves.append(name)
        flow.append(int(rate))
        connections.append(connect)
    return valves, flow, connections


if __name__ == "__main__":
    main()
