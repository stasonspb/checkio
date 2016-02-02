def break_rings(rings):
	rings = list(rings)
	new = []
	rez = 0
	while len(new) != len(rings):
		sorts = sort_links(rings)[0]
		print sort_links(rings)
		for ring in rings:
			if sorts in ring and len(ring) > 1:
				ring.remove(sorts)
				new.append(ring)
		rez += 1
	print rez
	return rez

def sort_links(rings):
	rings_sort = []
	[rings_sort.extend(ring) for ring in rings if len(ring) > 1]
	dicts = {k: rings_sort.count(k) for k in rings_sort}
	return sorted(dicts, key = lambda x: dicts.get(x), reverse = True)

break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},))
break_rings(({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},{10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},))



#if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    #assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    #assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    #assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
