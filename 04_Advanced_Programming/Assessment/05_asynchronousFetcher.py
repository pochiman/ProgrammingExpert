##### Asynchronous Fetcher #####

# Write a BatchFetcher class that is meant to fetch lots of records from a database very quickly.

# Your constructor takes in a database object that has an async method called async_fetch.
# This method takes a record identifier (or record_id) and returns whatever the database 
# has in storage for that record.

# BatchFetcher should implement the async method fetch_records, which takes in a list,
# record_ids, and should return the list of records corresponding to those record_ids.

# >>> fetcher = BatchFetcher(database)
# >>> fetcher.fetch_records(["A", "B", "C"])
# [{"data": "data of record A"}, {"data": "data of record B"}, {"data": "data of record C"}]

##### Solution 1 #####
# import asyncio


# class BatchFetcher:
#     def __init__(self, database):
#         self.database = database

#     async def fetch_records(self, record_ids):
#         pending_records = []
#         for record_id in record_ids:
#             pending_records.append(self.database.async_fetch(record_id))

#         return await asyncio.gather(*pending_records)

##### Solution 2 #####
import asyncio


class BatchFetcher:
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        pending_records = []
        for record_id in record_ids:
            task = asyncio.create_task(self.database.async_fetch(record_id))
            pending_records.append(task)

        records = []
        for pending_record in pending_records:
            records.append(await pending_record)
        return records