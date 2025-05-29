# --- 1. views.py ---
from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipment, EquipmentCategory, Cart, CartItem, Review
from django.contrib.auth.decorators import login_required

def store_view(request):
    category_slug = request.GET.get('category')
    equipment_list = Equipment.objects.filter(available=True)
    if category_slug:
        equipment_list = equipment_list.filter(category__slug=category_slug)
    categories = EquipmentCategory.objects.all()
    return render(request, 'store/store.html', {
        'equipment_list': equipment_list,
        'categories': categories,
    })

def equipment_detail_view(request, slug):
    item = get_object_or_404(Equipment, slug=slug)
    reviews = item.reviews.all()
    return render(request, 'store/equipment_detail.html', {
        'item': item,
        'reviews': reviews,
    })

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Equipment, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, equipment=item)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('store')

@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def leave_review(request, slug):
    item = get_object_or_404(Equipment, slug=slug)
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        comment = request.POST.get('comment', '')
        Review.objects.create(equipment=item, user=request.user, rating=rating, comment=comment)
        return redirect('equipment_detail', slug=slug)
    return redirect('equipment_detail', slug=slug)
