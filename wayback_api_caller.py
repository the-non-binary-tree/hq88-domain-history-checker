import sys
from datetime import datetime
from waybackpy import WaybackMachineCDXServerAPI
from waybackpy.exceptions import NoCDXRecordFound
import time

def get_oldest_capture(domain):
    user_agent = "Mozilla/5.0 (compatible; MyResearchBot/1.0)"
    cdx = WaybackMachineCDXServerAPI(url=domain, user_agent=user_agent)
    try:
        oldest = cdx.oldest()
        ts = oldest.timestamp
        formatted_date = f"{ts[6:8]}-{ts[4:6]}-{ts[:4]}"
        print(f"Kết quả xa nhất: {formatted_date}")
    except NoCDXRecordFound:
        print("Không tìm thấy capture nào cho domain này.")
        
def get_newest_capture(domain):
    user_agent = "Mozilla/5.0 (compatible; MyResearchBot/1.0)"

    cdx = WaybackMachineCDXServerAPI(url=domain, user_agent=user_agent)

    try:
        newest = cdx.newest()
        ts = newest.timestamp
        formatted_date = f"{ts[6:8]}-{ts[4:6]}-{ts[:4]}"
        print(f"Kết quả gần nhất: {formatted_date}")
    except NoCDXRecordFound:
        print("Không tìm thấy capture nào cho domain này.")


def get_capture_count(domain):
    user_agent = "Mozilla/5.0 (compatible; MyResearchBot/1.0)"

    cdx = WaybackMachineCDXServerAPI(url=domain, user_agent=user_agent)
    total_captures = sum(1 for _ in cdx.snapshots())
    print(f"Tổng số save time: {total_captures}")

if __name__ == "__main__":
    start = time.perf_counter()

    domain = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    print(f"Xử lý domain: {domain}")

    get_oldest_capture(domain)
    get_newest_capture(domain)
    get_capture_count(domain)
    
    end = time.perf_counter()
    print(f"Thời gian xử lý domain {domain}: {end - start:.6f} giây")
