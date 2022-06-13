from django.forms import model_to_dict
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Sum

from .models import Match, Trad, TicketCount


def get_match(request):
    match = Match.objects.all().latest("start_match_hour")

    m = model_to_dict(match)
    m["start_match_hour"] = datetime.timestamp(m["start_match_hour"])
    tickets_all = TicketCount.objects.filter(match=match).aggregate(Sum("amount"))
    tickets1 = TicketCount.objects.filter(match=match, bent_on="team1").aggregate(
        Sum("amount")
    )
    pourcent1 = tickets1["amount__sum"] * 100 / tickets_all["amount__sum"]
    tickets2 = TicketCount.objects.filter(match=match, bent_on="team2").aggregate(
        Sum("amount")
    )
    pourcent2 = tickets2["amount__sum"] * 100 / tickets_all["amount__sum"]
    ticketsnull = TicketCount.objects.filter(match=match, bent_on="null").aggregate(
        Sum("amount")
    )
    pourcentnull = ticketsnull["amount__sum"] * 100 / tickets_all["amount__sum"]

    m["team1_pourcentage"] = f"{pourcent1:.2f}"
    m["team2_pourcentage"] = f"{pourcent2:.2f}"
    m["null_pourcentage"] = f"{pourcentnull:.2f}"

    return JsonResponse(m)


def get_trad(request):
    trads = Trad.objects.all()
    trads_dict = {trad.key: trad.content for trad in trads}
    return JsonResponse(trads_dict)


def post_ticket(request):
    if request.method == "POST":
        import json

        body_unicode = request.body.decode("utf-8")
        data = json.loads(body_unicode)
        print("data")
        print(data)
        match = Match.objects.all().latest("start_match_hour")
        bent_on = "null"
        if data["wallet"] == match.team1_wallet:
            bent_on = "team1"
        if data["wallet"] == match.team2_wallet:
            bent_on = "team2"

        try:
            TicketCount.objects.create(
                match=match,
                address=data["wallet"],
                amount=data["amount"],
                bent_on=bent_on,
            )
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)})
        return JsonResponse({"status": "ok"})
