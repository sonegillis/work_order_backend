from requests import Session
from getpass import getpass
from bs4 import BeautifulSoup as bs

print("************************************************************")
print("WRITTEN BY: MEKOLLE SONE GILLIS EKEH")
print("THIS IS A TESTING PROGRAM FOR THE HATCHWAYS ASSESSMENT API")
print("Follow the instructions below to test this api")
print("************************************************************")

global api_ip, api_port, parse_session
dict_options = {
    "1" : "create_worker",
    "2" : "delete_worker",
    "3" : "create_work_order",
    "4" : "assign_worker_an_order",
    "5" : "fetch_work_orders",
}

def prompt_ip_port():
    global api_ip, api_port
    api_ip = input("Enter the IP address to the API location: ")
    api_port = input("Enter the PORT number of the API location: ")
    return (api_ip, api_port,)

def prompt_login():
    username = input("Username: ")
    password = getpass(prompt="Password: ")
    return (username, password,)

def login(url):
    username, password = prompt_login()
    payload = {"username": username, "password": password}
    global parse_session
    with Session() as session:
        parse_session = session
        login_page = session.get(url)
        page_content = bs(login_page.content, "html.parser")
        csrf_token = page_content.find("input", {"name":"csrfmiddlewaretoken"})["value"]
        payload.update({"csrfmiddlewaretoken": csrf_token})
        response = session.post(url, payload)

        if response.url == ("http://"+api_ip+":"+api_port+"/admin/"):
            return (True, session)
        else:
            return (False, None)

def create_worker():
    url = "http://{}:{}/api/create/worker/".format(api_ip, api_port)
    name = input("Name: ")
    company_name = input("Company name: ")
    email = input("Email: ")
    payload = {"name": name, "company_name": company_name, "email": email}

    with Session() as session:
        session = parse_session
        response = session.post(url, json=payload)
        print("\n\n")
        print(response.content)
        print("\n\n")

def delete_worker():
    worker_id = input("Enter worker ID: ")
    url = "http://{}:{}/api/delete-worker/{}/".format(api_ip, api_port, worker_id)
    with Session() as session:
        session = parse_session
        response = session.delete(url)
        print("\n\n")
        print(response.content)
        print("\n\n")

def create_work_order():
    url = "http://{}:{}/api/create/work-order/".format(api_ip, api_port)
    title = input("Title: ")
    description = input("Description: ")
    deadline = input("Deadline (Format: yyyy-mm-dd): ")
    payload = {"title": title, "description": description, "deadline": deadline}
    
    with Session() as session:
        session = parse_session
        response = session.post(url, json=payload)
        print("\n\n")
        print(response.content)
        print("\n\n")

def assign_worker_an_order():
    worker_id = input("Enter worker ID: ")
    work_order_id = input("Enter work order ID: ")
    url = "http://{}:{}/api/assign-worker-an-order/{}/{}/".format(api_ip, api_port, worker_id, work_order_id)
    with Session() as session:
        session = parse_session
        response = session.post(url)
        print("\n\n")
        print(response.content)
        print("\n\n")

def fetch_work_orders():
    worker_id = input("Enter worker ID: ")
    url ="http://{}:{}/api/get/work-orders/{}/".format(api_ip, api_port, worker_id)
    with Session() as session:
        session = parse_session
        response = session.get(url)
        print("\n\n")
        print(response.content)
        print("\n\n")
    
def main():
    ip, port = prompt_ip_port()
    url = "http://{}:{}/admin/login/?next=/admin/".format(ip, port)
    has_logged_in, session = login(url)
    while not has_logged_in:
        print("\n\nWrong Username and Password combination\n\n.Try Again....\n")
        session, has_logged_in = login(url)

    choice = """
                SELECT OPTION
                1. Create a worker
                2. Delete a worker
                3. Create a work order
                4. Assign a worker to an order
                5. Fetch work orders for a worker \n
            """

    while True:
        option = input(choice)
        eval(dict_options[option]+"()")

if __name__ == '__main__':
    main()
