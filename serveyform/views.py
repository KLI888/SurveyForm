from django.shortcuts import render, redirect
from .models import MainCategory, SubCategory, SurveyOfficer, SurveyForm
import json

def home(request):
    survey_officer = SurveyOfficer.objects.all()
    main_category = MainCategory.objects.all()
    sub_category = SubCategory.objects.all()

    sub_categories_json = {
        category.main_category: [
            {"id": sub.sub_category, "text": sub.sub_category}
            for sub in sub_category if sub.main_category == category
        ]
        for category in main_category
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        legal_name = request.POST.get('legal_name')
        description = request.POST.get('description')
        main_category_name = request.POST.get('main_category')
        sub_category_name = request.POST.get('sub_category')
        upload_media = request.FILES.get('media_file')
        owner_name = request.POST.get('owner_name')
        owner_number = request.POST.get('owner_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        survey_taken_by_id = request.POST.get('survey_taken_by')
        mediclaim_validity = request.POST.get('mediclaim_validity')
        current_location = request.POST.get('current_location')  # Assuming location is stored here

        try:
                
            main_category = MainCategory.objects.get(main_category=main_category_name)
            sub_category = SubCategory.objects.get(sub_category=sub_category_name)
            survey_officer = SurveyOfficer.objects.get(surver_officer_id=survey_taken_by_id)
        except:
            pass

        survey_form = SurveyForm(
            name=name,
            legal_name=legal_name,
            description=description,
            main_category=main_category,
            sub_category=sub_category,
            upload_media=upload_media,
            owner_name=owner_name,
            owner_number=owner_number,
            email=email,
            address=address,
            survey_officer=survey_officer,
            mediclaim=mediclaim_validity,
            current_location=current_location
        )

        survey_form.save()

        return redirect('/')  # Replace 'success_page' with your actual success page URL name

    google_form_api_key = "AIzaSyC2JQykAtfO8DVSwXnqKxVG_OzJCxryJf0"

    context = {
        'gmap_api': google_form_api_key,
        'survey_officer': survey_officer,
        'main_category': main_category,
        'sub_categories_json': json.dumps(sub_categories_json),
    }

    return render(request, 'index.html', context)
