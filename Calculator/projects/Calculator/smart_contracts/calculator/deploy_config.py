import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
# algod_client : connects with client of block chain network
# indexer_client : reads block chzin data
# app_spec : ARC32 JSON file application binary interface(ABI) contains all specifications and properties
# deployer : account for creating
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.calculator.calculator_client import (
        CalculatorClient,
    )
    #Initialize algo_client, indexer_client, to run and deploy in testnet
                                    #token      testnet address   
    testnetAlgodClient = AlgodClient("a" * 64, "https://testnet-api.algonode.cloud")
    testnetIndexerClient = IndexerClient("a" * 64, "https://testnet-idx.algonode.cloud")
    myAccount = algokit_utils.get_account_from_mnemonic("hundred useful snake trumpet skirt melt payment limb spider blame adapt chaos stumble vanish voyage gold episode age monitor breeze true switch orbit absorb rhythm")

    #Change when testnet is used
    app_client = CalculatorClient(
        algod_client = testnetAlgodClient,
        creator=myAccount,
        indexer_client=testnetIndexerClient,
    )
# Deploying of the application
    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )


    logger.info(f"Deployed Calculator with App ID: {app_client.app_id}")
    a = 10 
    b = 7
    response = app_client.add(a = a, b = b)
    logger.info(
        f"Called add on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a = {a} and b = {b} received: {response.return_value}"
    )

    a = 10 
    b = 7
    response = app_client.sub(a = a, b = b)
    logger.info(
        f"Called sub on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a = {a} and b = {b} received: {response.return_value}"
    )

    a = 10 
    b = 7
    response = app_client.mul(a = a, b = b)
    logger.info(
        f"Called mul on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a = {a} and b = {b} received: {response.return_value}"
    )

    a = 10 
    b = 7
    response = app_client.div(a = a, b = b)
    logger.info(
        f"Called div on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a = {a} and b = {b} received: {response.return_value}"
    )
