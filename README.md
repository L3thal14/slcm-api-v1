# Student Management System API

A Web Application built using Flask to get the marks,attendance and upcoming calendar activities with Captcha bypass from [SLCM Website](https://slcm.manipal.edu) .

## Steps to Install

```bash
     git clone https://github.com/l3thal14/slcm-api-v1
```

```bash
     cd slcm-api-v1
```

```python
     pip install -r requirements.txt
```

```bash
     python3 slcm.py
```

### Make a Request

#### CLI

```bash
  curl --location --request POST 'http://127.0.0.1:5000/api/v1/post' \
--header 'Content-Type: application/json' \
--data-raw '{Request Variables}'
```

### Request Format

The server expects requests to be in the following format:

```JSON
{
    "username" : "<SLCM Username>",
    "password" : "<SLCM Password>",
    "type": "<TYPE>"
}
```

Type can be set to `ATTENDANCE` , `MARKS`, `CALENDAR` or `ALL` depending on what is required.

NOTE: `ALL` request returns the Name of the student, SLCM Profile Image url, Attendance, Marks and Calendar Activity.

## Response

```JSON
{
    "attendance": [
        {
            "Academic Year": "2020-2021",
            "Attendance(%)": "100.00",
            "Days Absent": "0",
            "Days Present": "36",
            "Semester/Year": "V",
            "Subject": "XXXX",
            "Subject Code": "XXX",
            "Total Class": "36"
        },
        {
            "Academic Year": "2020-2021",
            "Attendance(%)": "100.00",
            "Days Absent": "0",
            "Days Present": "48",
            "Semester/Year": "V",
            "Subject": "XXXX",
            "Subject Code": "XXX",
            "Total Class": "48"
        }
    ],
    "calendar": [
        {
            "Date": "3   M",
            "End Date": "21 Nov 2020",
            "Notice": "Odd Semester Classes ",
            "Start Date": "03 Aug 2020",
            "Total Days": "111D"
        },
        {
            "Date": "11   F",
            "End Date": "20 Dec 2020",
            "Notice": "Registering for End Sem Exams(applicable only forstudent admitted prior to2014) ",
            "Start Date": "11 Dec 2020",
            "Total Days": "10D"
        }
    ],
    "imageurl": "https://slcm.manipal.edu/imagereader.aspx?FileName=&ImagePath=E:\\PortalDocuments\\XXXXXXXXXXXX.jpg",
    "marks": "<table>HTML Code</table>",
    "name": "Example"
}
```

Incase all are requested together, they are concatenated into a single JSON Object just like the example above.
