import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def calculate_eco_score(product):
    score = 100

    packaging = product.get("packaging", "").lower()
    categories = product.get("categories", "").lower()
    labels = product.get("labels", "").lower()

    # Packaging impact
    if "plastic" in packaging:
        score -= 25
    elif "glass" in packaging:
        score -= 10
    elif "paper" in packaging:
        score -= 5

    # Category impact
    if "soft drink" in categories:
        score -= 10
    if "beverage" in categories:
        score -= 5

    # Eco bonus
    if "vegetarian" in labels:
        score += 5

    score = max(0, min(score, 100))

    return score

@api_view(["GET"])
def get_product(request):
    barcode = request.GET.get("barcode")
    if not barcode:
        return Response({"error": "Barcode required"}, status=400)

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    res = requests.get(url)

    if res.status_code != 200:
        return Response({"error": "Product not found"}, status=404)

    data = res.json()
    product = data.get("product", {})

    if not product:
        return Response({"error": "Invalid product"}, status=404)

    return Response({
                "product_name": product.get("product_name"),
        "brand": product.get("brands"),
        "quantity": product.get("quantity"),
        "categories": product.get("categories"),
        "packaging": product.get("packaging"),
        "packaging_tags": product.get("packaging_materials_tags", []),
        "eco_score": calculate_eco_score(product),
        "image": product.get("image_front_url"),
        "suggestion": "Switch to eco-friendly packaging for lower impact"

    })