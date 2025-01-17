from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/parkedwards/prefect-testbed.git",
        entrypoint="flows/managed-exec-print-ip.py:print_my_ip",
    ).deploy(
        name="print-my-ip",
        work_pool_name="managed-execution-static-ip",
    )