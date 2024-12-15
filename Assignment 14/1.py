from google.colab import drive
def mount_drive():
    try:
        drive.mount('/content/drive')
        print("Drive mounted successfully")
        return True
    except Exception as e:
        print(f"Error mounting drive: {str(e)}")
        return False
if __name__ == "__main__":
    mount_drive()
