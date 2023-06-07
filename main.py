from website import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)

#ctrl+shift+p, type "python, select interpreter 3.8.3 64-bit (conda)"