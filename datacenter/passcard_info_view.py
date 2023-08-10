from django.utils.timezone import localtime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visit = Visit()
    visits = Visit.objects.filter(passcard=passcard)
    visit_duration = []
    for visit_data in visits:
        if not visit_data.leaved_at:
            continue
        duration_in_sec = visit.get_duration(visit_data.entered_at, visit_data.leaved_at)
        duration = visit.format_duration(seconds=duration_in_sec)
        visit_duration.append(duration)

    this_passcard_visits = []
    for visit_data, duration in zip(visits, visit_duration):
        this_passcard_visits.append({
            'entered_at': localtime(visit_data.entered_at),
            'duration': f'{duration["hours"]:02d}:{duration["minutes"]:02d}:{duration["seconds"]:02d}',
            'is_strange': visit.is_visit_long(visit.get_duration(visit_data.entered_at, visit_data.leaved_at))
        }),

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
