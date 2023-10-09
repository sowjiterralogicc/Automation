import os
from datetime import datetime
#A Simple Content Management System (CMS) is a software application or platform that allows users to create,
# manage, and modify digital content on a website without requiring advanced technical skills
def create_blog_post():
    title = input("Enter the title of the blog post: ")
    content = input("Enter the content of the blog post: ")

    # Generate a unique filename based on the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.txt"

    # Save the blog post as a text file
    with open(filename, "w") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Date: {timestamp}\n\n")
        file.write(content)

create_blog_post()
def list_blog_posts():
  blog_posts = [file for file in os.listdir() if file.endswith(".txt")]
  return blog_posts
def read_blog_post(filename):
  with open(filename, "r") as file:
    return file.read()
def view_blog_posts():
  blog_posts = list_blog_posts()
  if not blog_posts:
    print("No blog posts found.")
    return

  print("Available Blog Posts:")
  for i, post in enumerate(blog_posts, start=1):
    print(f"{i}. {post}")

  choice = input("Enter the number of the post you want to read: ")
  try:
    choice = int(choice)
    print("choice::::::::",choice)
    if 1 <= choice <= len(blog_posts):
      print("blog_posts:::::::::",blog_posts)
      print("len(blog_posts:::::::::",len(blog_posts))
      selected_post = blog_posts[choice - 1]
      print("selected_post:::::::::",selected_post)
      content = read_blog_post(selected_post)
      print("content::::::::",content)
      print(f"\n{content}")
    else:
      print("Invalid choice.")
  except ValueError:
    print("Invalid input. Please enter a number.")

view_blog_posts()

def edit_blog_post(filename):
  with open(filename, "r") as file:
    content = file.read()

  print(f"Editing: {filename}")
  print(f"Current content:\n{content}\n")

  new_content = input("Enter the new content for the blog post: ")

  with open(filename, "w") as file:
    file.write(content)  # Overwrite with the new content


def edit_existing_blog_post():
  blog_posts = list_blog_posts()
  if not blog_posts:
    print("No blog posts found.")
    return

  print("Available Blog Posts:")
  for i, post in enumerate(blog_posts, start=1):
    print(f"{i}. {post}")

  choice = input("Enter the number of the post you want to edit: ")
  try:
    choice = int(choice)
    if 1 <= choice <= len(blog_posts):
      selected_post = blog_posts[choice - 1]
      edit_blog_post(selected_post)
      print("Blog post edited successfully.")
    else:
      print("Invalid choice.")
  except ValueError:
    print("Invalid input. Please enter a number.")

edit_existing_blog_post()
