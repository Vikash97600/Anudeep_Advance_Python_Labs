# 1. You have a list of user data with their names and email addresses. Create a
# dictionary that maps each domain (from the email address) to a list of users with
# emails from that domain.


users = [
{"name": "Vikash", "email": "vikash@gmail.com"},
{"name": "Hitesh", "email": "hitesh@outlook.com"},
{"name": "Anchal", "email": "anchal@gmail.com"},
{"name": "Anshu", "email": "anshu@outlook.com"},
]


domain_users = {
domain: [item['name'] for item in users if item['email'].endswith(domain)]
for domain in {item['email'].split('@')[1] for item in users}
}
for i,j in domain_users.items():
    print(i,j)



# 2. You have a list of customer reviews for different products. Each review
# contains a product name and a rating. Your task is to create a dictionary that
# maps each product to its average rating.

reviews = [
{'product': 'Laptop', 'rating': 5},
{'product': 'Smartphone', 'rating': 4},
{'product': 'Laptop', 'rating': 3},
{'product': 'Tablet', 'rating': 4},
{'product': 'Smartphone', 'rating': 5}
]

product_ratings = {}

for review in reviews:
    product = review['product']
    rating = review['rating']
    if product not in product_ratings:
        product_ratings[product] = [rating]
    else:
       product_ratings[product].append(rating) 

for product, ratings in product_ratings.items():
    average_rating = sum(ratings) / len(ratings)
    print(f"Product: {product}, Average Rating: {average_rating}")

