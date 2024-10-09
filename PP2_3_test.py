import os.path
import sys
import PP2_3

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5', '5', '2']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_3.input = mock_input

	PP2_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: Input a number: Isosceles\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5', '3', '6']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_3.input = mock_input

	PP2_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: Input a number: Scalene\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP2_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1', '2', '4']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_3.input = mock_input

	PP2_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: Input a number: No Triangle\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP2_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['4.5', '4.5', '4.5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_3.input = mock_input

	PP2_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: Input a number: Equilateral\n"

