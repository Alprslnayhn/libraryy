class Library:


        
    def add_book(self):
            name = input ("Enter the name of the book: ")
            author = input ("Enter the author of the book: ")
            number_of_page = input ("Enter the number of page of the book: ")
            history = input ("Enter the history of the book: ")
            newadd = name + "," + author + "," + number_of_page + "," + history
            f = open("myfile.txt", "+a")
            f.write(newadd + "\n")

    def remove_book(self):
        self.name = input ("Enter the name of the book: ")
        f = open("myfile.txt", "r")
        lines = f.readlines()
        f.close()
        f = open("myfile.txt", "w")
        for line in lines:
            if self.name not in line:
                f.write(line)
        f.close()
        print("The book is removed")
    

    def list_books(self):
        f = open("myfile.txt", "r")
        lines = f.readlines()
        for line in lines:
             title, author, release_date, num_pages = line.split(",")
             print(f"Title: {title}, Author: {author}")
        f.close()

def main():
    lib = Library()
    f = open("myfile.txt", "w")
    print("lutfen birseyler seciniz")
    
    while True:
          secim = input("1- list a books\n2- add a book\n3- remove books\n4- Quit\n seciminizi yapiniz:")

          if secim == "1":
                lib.list_books()
          elif secim == "2":
                lib.add_book()
          elif secim == "3":
                lib.remove_book()
          elif secim == "4": 
                print("Cikis yapiliyor")
                break
          else:
            print("Yanlis secim yaptiniz")

if __name__ == "__main__":
    main()
# aramada isim yazar 
# silmed isim sadece