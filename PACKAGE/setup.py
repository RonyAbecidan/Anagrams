from setuptools import setup

setup(name='Anagrams',
      version='0.1',
      description='Solving of 3 problems using anagrams',
      url='https://github.com/RonyAbecidan/Anagrams',
      author='Rony Abecidan',
      author_email='ronyabecidan@gmail.com',
      license='University of Lille',
      package=['First_problem','Second_problem','Third_Problem'],
	  install_requires=[
		  'numpy',
          'textdistance',
      ],
      python_requires='>=3.6',
      zip_safe=False)
	  
