'''
Program: 	host-blocker.py
Author:		James E.
Written:	2021/04/01
Description:	Adds and/or removes rules in the Windows 'hosts' file in order
		to block/unblock a list of defined domains. Originally written
		to prevent impulse clicking on social media. Must be run as
		admin in order to read/write the 'hosts' file (system32 file).

Written for Windows 10 version 19042
'''
import sys
import os

def main():

	file_path = r'C:\Windows\System32\drivers\etc\hosts'
	
	header = '# host-blocker.py entries'
	
	# Define Win 10 rules based on the following format:
	# <localhost ip> <www.website.tld> <website.tld>
	rule_list = [
	'127.0.0.1 news.ycombinator.com',
	'127.0.0.1 www.reddit.com reddit.com',
	'127.0.0.1 www.twitter.com twitter.com',
	'127.0.0.1 www.twitch.tv twitch.tv',
	'127.0.0.1 www.youtube.com youtube.com'
	]

	# Open 'hosts' file
	existing_rules = open_file(file_path)

	# Check if any rules from rule_list already exist, adds them otherwise.
	if check_rules(existing_rules, rule_list, header) == True:
		print('Found existing rule from rule_list. Removing all entries ...')
		revised_rules = remove_rules(existing_rules, rule_list, header)
	else:
		revised_rules = add_rules(existing_rules, rule_list, header)

	# Save hosts file with the modified data 
	save_file(file_path, revised_rules)

	# Flush DNS (optional)
	#os.system('ipconfig /flushdns')

	input('Press ENTER to continue ...')


def open_file(file_path):
	'''
	Takes given file path as string & opens the file.
	'''

	existing_rules = []

	try:
		with open(file_path, 'r') as file_data:
			for line in file_data:
				line = line.strip()
				line = line.rstrip()
				existing_rules.append(line)

		return(existing_rules)

	except:
		print(f'Failed to read in {file_path}.\nAre you running as admin?')
		input('Press ENTER to continue ...')
		sys.exit(0)

def check_rules(existing_rules, rule_list, header):
	'''
	Checks the existing rules list from the 'hosts' file for the header that
	proceeds any block rules. Returns true/false value based on result.
	'''
	if header in existing_rules:
		return True
	else:
		print('Failed to find any existing rules from the rule_list.')
		return False

def remove_rules(existing_rules, rule_list, header):
	'''
	Loop through the existing rules and append all non-related rules to
	the revised_rules list. When the header is found, ignore all rules
	until a newline is reached (indicates the end of the block list).
	'''
	revised_rules = []
	ignore_rule = False

	for rule in existing_rules:
		if rule == header:
			ignore_rule = True

		elif ignore_rule == True and rule == '\n':
			ignore_rule = False

		elif ignore_rule == False:
			revised_rules.append(rule)
	
	return revised_rules

def add_rules(existing_rules, rule_list, header):
	'''
	Add a header indicating the origin of the rules, the rules themselves,
	and a newline at the end of the new rules to indicate the end.
	'''
	existing_rules.append(header)

	# Add rules at the end of the list.
	for rule in rule_list:
		existing_rules.append(rule)
	
	return existing_rules

def save_file(file_path, revised_rules):
	try:
		with open(file_path, 'w') as file_data:
			for line in revised_rules:
				file_data.write(line + '\n')
			print('Rules successfully updated!')
	except:
		print(f'Failed to save {file_path}. Quitting ...')
		sys.exit(0)


if __name__ == '__main__':
	main()
