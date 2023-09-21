import re

try:
    # Read the input text file
    with open('text_file.txt', 'r') as file:
        text = file.read()

    # Regular expression pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # Find all email addresses in the text
    email_addresses = re.findall(email_pattern, text)

    print("Email addresses found:")
    for email in email_addresses:
        print(email)

    # Remove duplicates from the list of email addresses
    unique_email_addresses = list(set(email_addresses))

    # Store the extracted email addresses in a separate text file
    # with open('extracted_emails.txt', 'w') as output_file:
    #     for email in unique_email_addresses:
    #         output_file.write(email + '\n')
    #
    # print("Unique email addresses extracted and saved to 'extracted_emails.txt'.")
    print(unique_email_addresses)

except FileNotFoundError:
    print("Error: The input file 'text_file.txt' was not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")



# import re
#
# # Read the input text file
# with open('text_file.txt', 'r') as file:
#     text = file.read()
#
# # Regular expression pattern to match email addresses
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#
# # Find all email addresses in the text
# email_addresses = re.findall(email_pattern, text)
# print(email_addresses)
# for email in email_addresses:
#     print(email)
# str=" ".join(email_addresses)
# print(str)
# l=[]
# for email in email_addresses:
#     if email not in l:
#         l.append(email)
# print(l)
#
# # Store the extracted email addresses in a separate text file
# # with open('extracted_emails.txt', 'w') as output_file:
# #     for email in email_addresses:
# #         output_file.write(email + '\n')
#
# print("Email addresses extracted and saved to 'extracted_emails.txt'.")
