from rest_framework import serializers
from .models import EscapeQueue


class EscapeQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscapeQueue
        fields = "__all__"
        extra_kwargs = {
            "id": {"help_text": "예약 항목 ID"},
            "applicant_id": {"help_text": "유저의 ID"},
            "reason": {"help_text": "예약 사유"},
            "status": {
                "help_text": "예약 수락 여부 ex) 1 (1, 'accepted'),(2, 'denied'),(3, 'waiting'),(4, 'expired')"
            },
            "is_active": {"help_text": "활성화 된 유저인지 확인 (이메일 인증 여부) ex) 1"},
            "start_at": {"help_text": "외출 시작 시간 ex) 2021-06-18T02:01:59.856000Z"},
            "end_at": {"help_text": "외출 종료 시간 ex) 2021-06-18T02:01:59.856000Z"},
            "created_at": {"help_text": "외출 신청 시간 ex) 2021-06-18T02:01:59.856000Z"},
        }
