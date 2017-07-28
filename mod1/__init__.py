def test():
	import nose
	nose.main('mod1', 'mod1')
test.__test__ = False

def main():
	print("Running tests")
	test()
