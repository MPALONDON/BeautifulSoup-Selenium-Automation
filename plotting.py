import pandas as pd
import matplotlib.pyplot as plt

def create_graph(all_books):

    df_books = pd.DataFrame(all_books)

    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    df_books['rating'] = df_books['rating'].map(rating_map)

    df_books['price'] = df_books['price'].str.replace('£', '').str.strip().astype(float)

    df_books.to_csv('Data/books.csv', index=False)

    avg_price_by_rating = df_books.groupby('rating')['price'].mean()

    plt.figure(figsize=(6,4))
    plt.bar(avg_price_by_rating.index, avg_price_by_rating.values, color='orange')
    plt.xlabel("Rating")
    plt.ylabel("Average Price (£)")
    plt.title("Average Book Price by Rating")
    plt.xticks(range(1,6))
    plt.show()








