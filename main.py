
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


word_count_1=0
word_count_2=0
string_1="true"
string_2="love"
for i in string_1:
  ii=name1.count(i)
  kk=name2.count(i)
  
  word_count_1+=ii+kk
print(F"The word count in TRUE is  {word_count_1}")
for j in string_2:
  jj=name1.count(j)
  nn=name2.count(j)
  word_count_2+=jj+nn
print(F"The word count in LOVE is  {word_count_2}")
print(f"your love score is {word_count_1}{word_count_2}")
# `name1 = "Angela Yu"`

# `name2 = "Jack Bauer"`

  
  
  

    


