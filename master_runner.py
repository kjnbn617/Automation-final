import subprocess

scripts_to_run = [
    "BeatPlanReport/BeatPlanReport.py",
    "BeatVisitReport/BeatVisitReport.py",
    "DailyB2CSalesReport/DailyB2CSalesReport.py",
    "DailyMFISalesReport/DailyMFISalesReport.py",
    "DLEWiseSalesReport/DLEWiseSalesReport.py"
]

for script in scripts_to_run:
    print(f"Running: {script}")
    subprocess.run(["python", script], check=True)
