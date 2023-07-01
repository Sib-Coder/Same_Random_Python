
def decorator(funct):
    def wraper(text):
        print("New information")
        funct(text)
    return wraper

@decorator
def test(text):
    print(f"Same text :{text}")


def main():
    test("daniil love")

if __name__ == "__main__":
	main()