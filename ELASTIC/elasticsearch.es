# 0712 mission
# 은행별 보유 갯수, 평균고객수 집계
GET bank/_search
{
  "size": 0,
  "aggs": {
    "bank": {
      "terms": {
        "field": "bank.keyword"
      },
      "aggs": {
        "avg_cp": {
          "avg": {
            "field": "customers"
          }
        }
      }
    }
  }
}

# date 값을 1개월 간격의 버킷으로 구분
GET bank/_search
{
  "size": 0,
  "aggs": {
    "date_his": {
      "date_histogram": {
        "field": "date",
        "interval": "month"
      }
    }
  }
}


# 국민은행 강남점 검색
GET bank/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "location": "강남"
          }
        },
        {
          "match": {
            "bank": "국민은행"
          }
        }
      ]
    }
  }
}


# 강남지역 은행이용하는 평균 고객수
GET bank/_search
{
  "size": 0,
  "query": {
    "match": {
      "location": "강남"
    }
  },
  "aggs": {
    "c_su": {
      "avg": {
        "field": "customers"
      }
    }
  }
}
