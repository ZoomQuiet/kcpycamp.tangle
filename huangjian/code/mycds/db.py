def read(filename):
    records = []
    try:
        for line in open(filename):
            records.append(line.strip().split("#"))
    except IOError:
        pass
    return records

def save(records,filename):
    out = open(filename,'a')
    for items in records:
        out.write('#'.join(items)+'\n')
    out.close()

def edit(records,filename):
	out = open(filename,'w')
	for items in records:
		out.write('#'.join(items)+'\n')
	out.close()
