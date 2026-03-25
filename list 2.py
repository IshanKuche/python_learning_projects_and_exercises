
def merge_task(normal,urgent,merged_list):
    merged_list.extend(urgent)
    merged_list.extend(normal)

def display_task(merged_list):
    for task in merged_list:
        print(task)


def main():
    normal_task = ["bath","eat","shit","sleep"]
    urgent_task = ["project","journal","shopping"]
    merged_list = []
    merge_task(normal_task,urgent_task,merged_list)
    display_task(merged_list)

if __name__ == "__main__":
    main()