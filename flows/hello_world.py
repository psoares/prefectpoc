import prefect
from prefect import task, Flow
from prefect.storage import GitHub


@task(name="hello")
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")


with Flow("hello-flow") as flow:
    hello_task()

flow.storage = GitHub(repo="psoares/prefectpoc", path="/flows/hello_world.py")


if __name__ == '__main__':
    flow.run()
