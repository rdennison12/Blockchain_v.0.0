import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS

blockchain = Blockchain()

times = []

try:
    print("Program running... Press Ctrl+C to stop.")
    for i in range(1000):
        start_time = time.time_ns()
        blockchain.add_block(i)
        end_time = time.time_ns()

        time_to_mine = (end_time - start_time) / SECONDS
        times.append(time_to_mine)
        average_time = sum(times) / len(times)

        print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
        print(f'Time to mine a new block: {time_to_mine}s')
        print(f'Average time to add blocks: {average_time}s\n')
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Terminating gracefully.")
except Exception as e:
    print(f"An unexpected error has occurred: {e}")
