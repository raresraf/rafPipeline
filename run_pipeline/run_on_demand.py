import json
import os
import subprocess
import sys

TIMEOUT_RUN_ON_DEMAND = 10 * 60


def run_pipeline(atomic, solution_path, problemID):
    print(f"{problemID}: Running pipeline for {solution_path}. Atomic: {atomic}")
    for root, dirs, files in os.walk(f"../../TheInputsCodeforces/{problemID}"):
        for name in files:
            if '.DAT' not in name:
                continue

            input_path = (os.path.join(root, name))
            input_size = int(name[:-4])

            output_path = solution_path.replace("TheCrawlCodeforces",
                                                f"TheOutputsCodeforces/atomic_{atomic}") + f"/{input_size}.OUT"
            try:
                subprocess.call([f"./atomics/run_atomic_{atomic}.sh", solution_path, input_path, output_path],
                                shell=False, timeout=TIMEOUT_RUN_ON_DEMAND)
            except Exception as e:
                print(f"Exception for {output_path}: {e}")


if __name__ == "__main__":
    print("===== Run on-demand pipeline script =====")
    if len(sys.argv) != 3:
        print("Usage: python3 run_on_demand <problemID> <atomic_name>")
        print("Usage: <atomic_name> = 'all' to run all")
        sys.exit(1)

    problemID = sys.argv[1]
    atomic = sys.argv[2]
    with open("../dataset_metadata/codeforce_libc.json") as f:
        metadata = json.load(f)
        if not metadata.get(problemID, None):
            print(f"No solutions for <problemID>: {problemID}")
            sys.exit(1)

        for solution_path in metadata.get(problemID, None):
            if "all" == atomic.lower():
                # remove .CPP
                run_pipeline("perf", solution_path[:-4], problemID)
                run_pipeline("time", solution_path[:-4], problemID)
            else:
                # remove .CPP
                run_pipeline(atomic, solution_path[:-4], problemID)
