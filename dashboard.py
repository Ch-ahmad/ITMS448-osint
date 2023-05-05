# main_gui.py
import tkinter as tk
from tkinter import ttk
import praw
import datetime
from key_content import query_keywords
from tkinter import PhotoImage

client_id = '68n97pmuxvLUfkVHxU7w-w'
client_secret = 'bX25ZyAiK9Dg0-h423W5jQkRlDhArw'
user_agent = 'python:islfo:v1.0.0 (by /u/itm448)'
username = 'itm448'
password = 'Chicago12345!'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

def utc_to_local(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def search_posts(subreddit_name, query, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.search(query, limit=limit)

def search_and_display_results():
    subreddit_name = subreddit_entry.get()
    query = query_entry.get()
    limit = int(limit_entry.get())

    posts = search_posts(subreddit_name, query, limit)

    results.delete(1.0, tk.END)
    for post in posts:
        results.insert(tk.END, f"Author: {post.author}\n")
        results.insert(tk.END, f"Date posted: {utc_to_local(post.created_utc)}\n")
        results.insert(tk.END, f"Title (short description): {post.title}\n")
        results.insert(tk.END, f"Content link: {post.url}\n\n")

def show_reddit_tool():
    reddit_tool.tkraise()

app = tk.Tk()
app.title("Osint Tool")

# Create dashboard frame
dashboard = ttk.Frame(app)
dashboard.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create Reddit tool frame
reddit_tool = ttk.Frame(app, padding="10")
reddit_tool.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dashboard content
dashboard_title = ttk.Label(dashboard, text="Dashboard", font=("Helvetica", 18))
dashboard_title.grid(row=0, column=0, pady=(10, 20))

# Load the Reddit icon
reddit_icon = PhotoImage(file="reddit_icon.png")

# Create the button with the icon
reddit_button = ttk.Button(dashboard, image=reddit_icon, command=show_reddit_tool)
reddit_button.grid(row=1, column=0, pady=5)


# Reddit tool content
def display_dashboard():
    dashboard.tkraise()

# Add this function after the display_reddit_tool() function

# Create a back button in the Reddit tool content section

back_button = ttk.Button(reddit_tool, text="Back", command=display_dashboard)
back_button.grid(row=6, column=0, columnspan=2, pady=10)

tool_title = ttk.Label(reddit_tool, text="Reddit Search Tool", font=("Helvetica", 18))
tool_title.grid(row=0, column=0, columnspan=2, pady=(10, 20))

subreddit_label = ttk.Label(reddit_tool, text="Subreddit:")
subreddit_label.grid(row=1, column=0, sticky=tk.W)
subreddit_entry = ttk.Entry(reddit_tool)
subreddit_entry.grid(row=1, column=1)

query_label = ttk.Label(reddit_tool, text="Query:")
query_label.grid(row=2, column=0, sticky=tk.W)
query_entry = ttk.Entry(reddit_tool)
query_entry.grid(row=2, column=1)

limit_label = ttk.Label(reddit_tool, text="Limit:")
limit_label.grid(row=3, column=0, sticky=tk.W)
limit_entry = ttk.Entry(reddit_tool)
limit_entry.grid(row=3, column=1)

search_button = ttk.Button(reddit_tool, text="Search", command=search_and_display_results)
search_button.grid(row=4, column=0, columnspan=2, pady=10)

results = tk.Text(reddit_tool, wrap=tk.WORD, width=80, height=20)
results.grid(row=5, column=0, columnspan=2, pady=(10, 20))

# Set dashboard as the initial frame
dashboard.tkraise()

# Run the app
app.mainloop()
