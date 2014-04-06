import pickle

def list_pickler(lst, fil_name):
	
	fil = open(fil_name, 'wb')
	pickle.dump(lst, fil)
	fil.close()
	
def unpickler(fil_name):
	
	pkl_file = open(fil_name, 'rb')
	lst = pickle.load(pkl_file)
	pkl_file.close()
	return lst
	