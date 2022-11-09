from matplotlib import pyplot as plt

movies = ["Anna Hall", "Ben Hur", "Casablanca", "Gandhi", "West Side Story"]

num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], height [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favourite Movies")
plt.ylabel("# of Academy Awards")

# label x-axis with movies name at bar centers
plt.xticks(range(len(movies)), movies)



plt.show()

