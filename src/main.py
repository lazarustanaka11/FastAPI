from fastapi import FastAPI, Path, HTTPException, Query, Request
from .models import Customer, UpdateCustomer


app = FastAPI()

# temporarily storing in memory, NB: Implement Postgres Database
customers = {}


@app.get("/")
def home(request: Request):
    """
    Displays the list of all customers
    """
    return customers


@app.get("/get-customer/{customer_id}")
def get_customer(
    customer_id: int = Path(None, description="ID of customer you want to view", gt=0)
):
    if customer_id in customers:
        return customers[customer_id]
    raise HTTPException(status_code=404, detail="Customer Not Found")


@app.post("/create-customer/{customer-id}")
def create_customer(customer_id: int, customer: Customer) -> dict:
    """

    Args:
        customer_id (int):
        customer (Customer):

    Raises:
        HTTPException: [Customer Already Exists]

    Returns:
        JSon: [Created Customer]
    """
    if customer_id in customers:
        raise HTTPException(status_code=400, detail="Customer Already Exists")

    customers[customer_id] = customer
    return customers[customer_id]


@app.put("/create-customer/{customer-id}")
def update_customer(customer_id: int, customer_update: UpdateCustomer):
    """
    Args:
        customer_id (int)
        customer_update (UpdateCustomer)

    Raises:
        HTTPException: [Customer not Found]

    Returns:
        [JSon]: [modified customer]
    """
    if customer_id not in customers:
        raise HTTPException(status_code=404, detail="Customer not found")
    if customer_update.name != None:
        customers[customer_id].name = customer_update.name
    if customer_update.representative != None:
        customers[customer_id].representative = customer_update.representative
    if customer_update.contract_start != None:
        customers[customer_id].contract_start = customer_update.contract_start
    if customer_update.Branches != None:
        customers[customer_id].Branches = customer_update.Branches
    if customer_update.Country != None:
        customers[customer_id].Country = customer_update.Country
    return customers[customer_id]


@app.delete("/delete-customer")
def delete_customer(
    customer_id: int = Query(..., description="ID of customer to be deleted")
):
    """[summary]

    Args:
        customer_id (int):

    Raises:
        HTTPException: [Customer Not Found]
    """
    if customer_id not in customers:
        raise HTTPException(
            status_code=404, detail="The requested customer could not be found"
        )

    del customers[customer_id]
    return {"Data": "Customer has been successfully deleted!"}
