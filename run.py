from App.app import create_app

main = create_app()
if __name__ == "__main__":
	main.run(debug=True)