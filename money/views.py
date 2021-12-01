from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import FinancialMemo
from .serializers import FinancialMemoSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def create_or_read(request):
    # 모든 메모들 
    if request.method == 'GET':
        # 유저가 작성한 메모글
        financial_memos = request.user.financialmemo_set.all().filter(is_deleted = False)
        financial_memos_serializer = FinancialMemoSerializer(financial_memos, many = True)
        return Response(financial_memos_serializer.data)
    
    else:
        # post 요청이면 
        # 모델 만들어 디비에 저장 
        financial_memo_serializer = FinancialMemoSerializer(data = request.data)

        if financial_memo_serializer.is_valid(raise_exception = True):
            financial_memo_serializer.save(user = request.user)
            return Response(financial_memo_serializer.data, status = status.HTTP_201_CREATED)
    
    

@api_view(['PUT', 'DELETE', 'GET'])
def put_delete_get(request, memo_pk):
    
    # 타겟 메모 
    financial_memo = get_object_or_404(FinancialMemo, pk = memo_pk)
    
    # 삭제된 메모를 복구하는 경우가 아니면, 빈 페이지 리턴  
    if financial_memo.is_deleted == True and request.method != 'PUT':
        return Response({'id': memo_pk, 'is_deleted': True}, status = status.HTTP_204_NO_CONTENT)

    # 디테일 get  
    if request.method == 'GET':
        financial_memo_serializer = FinancialMemoSerializer(financial_memo)
        return Response(financial_memo_serializer.data)
    
    # 수정
    # 1. 삭제 요청
    # 2. 정보 수정  
    # 3. 삭제된 메모 복구 
    elif request.method == 'PUT':
        is_deleted = request.data.get('isDeleted')

        financial_memo_serializer = FinancialMemoSerializer(financial_memo, data = request.data)
        if financial_memo_serializer.is_valid(raise_exception = True):
            financial_memo_serializer.save()
        
        # 삭제된 메모 복구 혹은 메모 수정 요청 
        if is_deleted == False:
                return Response(financial_memo_serializer.data)            
        
        # 메모 삭제 요청 
        else:
            return Response({'id': memo_pk, 'is_deleted': True}, status = status.HTTP_204_NO_CONTENT)
    