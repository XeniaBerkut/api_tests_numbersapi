data_get_math_fact = [
  {
    "test_case_title": "Number: 1",
    "number": 1
  },
  {
    "test_case_title": "Number: 0",
    "number": 0
  },
  {
    "test_case_title": "Number: -23",
    "number": -23
  },
  {
    "test_case_title": "Number: 9999999999999999",
    "number": 9999999999999999
  },
  {
    "test_case_title": "Number: 9999999999999998",
    "number": 9999999999999998
  },
  {
    "test_case_title": "Number: -9999999999999999",
    "number": -9999999999999999
  },
  {
    "test_case_title": "Number: -9999999999999998",
    "number": -9999999999999998
  }
]

data_get_math_fact_rational = '3.14'


data_random_number_in_interval = [
  {
    "test_case_title": "Interval: from 99 to 100",
    "data": {
      "min": 99,
      "max": 100
    }
  },
  {
    "test_case_title": "Interval: from 6 to 6",
    "data": {
      "min": 6,
      "max": 6
    }
  },
  {
    "test_case_title": "Interval: from -9999999999999999 to 9999999999999999",
    "data": {
      "min": -9999999999999999,
      "max": 9999999999999999
    }
  }
]

data_random_number_min_more_than_max = {"min": 600, "max": 6}

data_post_submit_new_fact = {
          "text": "New info for 26",
          "number": "26",
          "type": "trivia"
        }


data_post_submit_bad_request = {
        "headers": {
          "Host": "http://numbersapi.com"
        },
        "body": {
          "text": "New info for 20626",
          "number": "20626",
          "type": "trivia"
        }
}
