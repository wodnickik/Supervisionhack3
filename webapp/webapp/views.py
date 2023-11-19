from django.db.models import Avg, StdDev, Q
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import BankOffer
from django.core import serializers
from .serializers import BankOfferSerializer, QuerySerializer
import pandas as pd
from django.http import JsonResponse


@api_view(['GET'])
def get_all_offers(request):
    all_offers = BankOffer.objects.all()

    all_deposits_for_people_pln = all_offers.filter(offer_type__exact="Lokata", client_type__exact="Indywidualny",
                                                    currency__exact="PLN")
    all_deposits_for_people_not_pln = all_offers.filter(~Q(currency="PLN"), offer_type__exact="Lokata",
                                                        client_type__exact="Indywidualny")

    all_deposits_for_firms_pln = all_offers.filter(offer_type__exact="Lokata", client_type__exact="Biznesowy",
                                                   currency__exact="PLN")
    all_deposits_for_firms_not_pln = all_offers.filter(~Q(currency="PLN"), offer_type__exact="Lokata",
                                                       client_type__exact="Biznesowy")

    all_accounts_for_people_pln = all_offers.filter(offer_type__exact="Konto oszczędnościowe",
                                                    client_type__exact="Indywidualny", currency__exact="PLN")
    all_accounts_for_people_not_pln = all_offers.filter(~Q(currency="PLN"), offer_type__exact="Konto oszczędnościowe",
                                                        client_type__exact="Indywidualny")
    all_accounts_for_firms_pln = all_offers.filter(offer_type__exact="Konto oszczędnościowe",
                                                   client_type__exact="Biznesowy", currency__exact="PLN")
    all_accounts_for_firms_not_pln = all_offers.filter(~Q(currency="PLN"), offer_type__exact="Konto oszczędnościowe",
                                                       client_type__exact="Biznesowy")

    average_dep_ppl_pln = list(all_deposits_for_people_pln.aggregate(Avg('interest')).values())[0]
    average_dep_ppl_not_pln = list(all_deposits_for_people_not_pln.aggregate(Avg('interest')).values())[0]
    average_dep_firm_pln = list(all_deposits_for_firms_pln.aggregate(Avg('interest')).values())[0]
    average_dep_firm_not_pln = list(all_deposits_for_firms_not_pln.aggregate(Avg('interest')).values())[0]
    average_acc_ppl_pln = list(all_accounts_for_people_pln.aggregate(Avg('interest')).values())[0]
    average_acc_ppl_not_pln = list(all_accounts_for_people_not_pln.aggregate(Avg('interest')).values())[0]
    average_acc_firm_pln = list(all_accounts_for_firms_pln.aggregate(Avg('interest')).values())[0]
    average_acc_firm_not_pln = list(all_accounts_for_firms_not_pln.aggregate(Avg('interest')).values())[0]

    std_dep_ppl_pln = list(all_deposits_for_people_pln.aggregate(StdDev('interest')).values())[0]
    std_dep_ppl_not_pln = list(all_deposits_for_people_not_pln.aggregate(StdDev('interest')).values())[0]
    std_dep_firm_pln = list(all_deposits_for_firms_pln.aggregate(StdDev('interest')).values())[0]
    std_dep_firm_not_pln = list(all_deposits_for_firms_not_pln.aggregate(StdDev('interest')).values())[0]
    std_acc_ppl_pln = list(all_accounts_for_people_pln.aggregate(StdDev('interest')).values())[0]
    std_acc_ppl_not_pln = list(all_accounts_for_people_not_pln.aggregate(StdDev('interest')).values())[0]
    std_acc_firm_pln = list(all_accounts_for_firms_pln.aggregate(StdDev('interest')).values())[0]
    std_acc_firm_not_pln = list(all_accounts_for_firms_not_pln.aggregate(StdDev('interest')).values())[0]

    all_deposits_for_people_pln = all_deposits_for_people_pln.filter(interest__gte=average_dep_ppl_pln + 3 * std_dep_ppl_pln)
    all_deposits_for_people_not_pln = all_deposits_for_people_not_pln.filter(interest__gte=average_dep_ppl_not_pln + 3 * std_dep_ppl_not_pln)
    all_deposits_for_firms_pln = all_deposits_for_firms_pln.filter(interest__gte=average_dep_firm_pln + 3 * std_dep_firm_pln)
    all_deposits_for_firms_not_pln = all_deposits_for_firms_not_pln.filter(interest__gte=average_dep_firm_not_pln + 3 * std_dep_firm_not_pln)
    all_accounts_for_people_pln = all_accounts_for_people_pln.filter(interest__gte=average_acc_ppl_pln + 3 * std_acc_ppl_pln)
    all_accounts_for_people_not_pln = all_accounts_for_people_not_pln.filter(interest__gte=average_acc_ppl_not_pln + 3 * std_acc_ppl_not_pln)

    if std_acc_firm_pln is not None:
        all_accounts_for_firms_pln = all_accounts_for_firms_pln.filter(interest__gte=average_acc_firm_pln + 3 * std_acc_firm_pln)
    if std_acc_firm_not_pln is not None:
        all_accounts_for_firms_not_pln = all_accounts_for_firms_not_pln.filter(interest__gte=average_acc_firm_not_pln + 3 * std_acc_firm_not_pln)

    all_deposits_for_people_pln.update(dangerous_indicator=True)
    all_deposits_for_people_not_pln.update(dangerous_indicator=True)
    all_deposits_for_firms_pln.update(dangerous_indicator=True)
    all_deposits_for_firms_not_pln.update(dangerous_indicator=True)
    all_accounts_for_people_pln.update(dangerous_indicator=True)
    all_accounts_for_people_not_pln.update(dangerous_indicator=True)
    all_accounts_for_firms_pln.update(dangerous_indicator=True)
    all_accounts_for_firms_not_pln.update(dangerous_indicator=True)

    sorted_orders = all_offers.order_by('-dangerous_indicator')
    serializer = BankOfferSerializer(sorted_orders, many=True)

    response = Response(serializer.data)
    response['Access-Control-Allow-Origin'] = '*'
    return response


@api_view(['GET'])
def get_plot_values(request):

    result = BankOffer.objects.values('bank_name', 'valid_from_date').annotate(dcount=Avg('interest')).order_by('valid_from_date')
    better_dict = {}
    for r in result:
        if r["bank_name"] not in better_dict.keys():
            better_dict[r["bank_name"]] = [[r["valid_from_date"]],[r["dcount"]]]
        else:
            better_dict[r["bank_name"]][0].append(r["valid_from_date"])
            better_dict[r["bank_name"]][1].append(r["dcount"])

    response = Response(better_dict)
    response['Access-Control-Allow-Origin'] = '*'
    return response


# Ręczne wczytywanie danych

# all_fields = ["bank_name",
#     "offer_name",
#     "interest",
#     "offer_type",
#     "offer_length_months",
#     "client_type",
#     "offer_kind",
#     "min_resources",
#     "max_resources",
#     "currency",
#     "additional_info",
#     "valid_from_date"]
#
# df = pd.read_excel("webapp/dane_generowane.xlsx")
# i = 1
# for row in df.iterrows():
#     # if i > 1:
#     #     break
#     value_dict = dict(zip(all_fields, row[1]))
#     # print(value_dict)
#     for key in value_dict.keys():
#         if pd.isna(value_dict[key]):
#             value_dict[key] = None
#     #
#     # if type(value_dict["valid_from_date"]) == str:
#     #     print('str true')
#     # if type(value_dict["valid_from_date"]) == datetime:
#     #     print('datetime true')
#     # print(value_dict["valid_from_date"])
#     if value_dict["valid_from_date"] is not None:
#
#         value_dict["valid_from_date"] = value_dict["valid_from_date"].strftime("%Y-%m-%d")
#     b = BankOffer(**value_dict)
#     b.save()
