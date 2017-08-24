m1 = ["m1"]
m2 = ["m2"]
m3 = ["m3"]

np1 = []
np2 = []
np3 = []
np4 = []

n_dict = {"0":np1, "1":np2, "2":np3, "3":np4}
m_dict = {"0":m1, "1":m2, "2":m3}

n_ctr = 0
while n_ctr < 4:
	m_ctr = 0
	while m_ctr < 3:
		n_dict[str(n_ctr)].append(m_dict[str(m_ctr)])
		m_ctr += 1
	print n_dict[str(n_ctr)]
	print
	n_ctr += 1
