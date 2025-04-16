from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def main(request):
    if request.method == "POST":
        subscribe_email = request.POST.get("subscribe-email")
        name = request.POST.get("name")
        send_mail(
            f"Γεια σου, {name}😉",
            "Αν ονειρεύεσαι την επόμενη απόδραση σου στην Κεφαλλονιά, τότε είσαι στο σωστό site! "
            "Εγγράψου στην σελίδα μας για να λαμβάνεις εξατομικευμένες ενημερώσεις και όλα τα μυστικά για να οργανώσεις το τέλειο ταξίδι στο πανέμορφο νησί μας.",
            "dimtakos86@gmail.com",
            [subscribe_email],
            fail_silently=False
        )

    return render(request, 'kefalonia/main_page.html',{})

def destinations(request):

    return render(request, 'kefalonia/destinations.html',{})