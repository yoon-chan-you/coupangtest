 쿠팡 테스트 케이스 (Coupang Test Cases)

## **사이트 정보**
- **테스트 대상 사이트**: [쿠팡](https://www.coupang.com)

---

## **테스트 시나리오**

### **로그인 기능 테스트**
#### **설명**
쿠팡 로그인 페이지에 접속한다.  
ID와 비밀번호를 입력한 후, 로그인 버튼을 클릭한다.  
로그인 성공 여부를 확인하기 위해 **로그아웃 버튼이 존재하는지 검사**한다.  
로그인 버튼 클릭 후, 로그인 창이 변경되는지 확인하고, 로그인 후 원래 페이지로 이동하는지도 검증한다.  

#### **구현 방식 및 사용 요소**
```python
# 로그인 페이지 이동
  driver.get(url)

# 페이지 로드 대기
  time.sleep(3) 또는 WebDriverWait(driver, 10)

# 로그인 필드 찾기
  driver.find_element(By.ID, "login-email-input")

# 비밀번호 입력
  driver.find_element(By.ID, "login-password-input")

# 입력값 전달
  .send_keys("test@example.com")

# 로그인 버튼 클릭
  driver.find_element(By.ID, "login-submit-btn").click()

# 로그인 성공 확인
  driver.find_element(By.ID, "logout-btn").is_displayed()
```

---

### **로그인 상태에서 검색 기능 테스트**
#### **설명**
로그인한 상태에서 검색 기능을 실행한다.  
검색어 **"노트북"**을 입력하고 검색 버튼을 클릭한다.  
검색 결과가 정상적으로 출력되는지 확인한다.  
검색 결과 리스트에서 **첫 번째 상품 제목**을 가져와 저장한다.  

#### **구현 방식 및 사용 요소**
```python
# 검색 입력 필드 찾기
  driver.find_element(By.ID, "search-input")

# 검색어 입력
  .send_keys("노트북")

# 검색 실행
  search_box.send_keys(Keys.RETURN)

# 검색 결과 대기
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-title")))

# 첫 번째 검색 결과 저장
  driver.find_element(By.CLASS_NAME, "product-title").text
```

---

### **비로그인 상태에서 검색 기능 테스트**
#### **설명**
로그아웃한 상태에서 검색 기능을 실행한다.  
검색어 **"노트북"**을 입력하고 검색 버튼을 클릭한다.  
검색 결과가 정상적으로 출력되는지 확인한다.  
검색 결과 리스트에서 **첫 번째 상품 제목**을 가져와 저장한다.  

#### **구현 방식 및 사용 요소**
```python
# 로그아웃 수행
  driver.find_element(By.ID, "logout-btn").click()

# 검색 입력 필드 찾기
  driver.find_element(By.ID, "search-input")

# 검색어 입력
  .send_keys("노트북")

# 검색 실행
  search_box.send_keys(Keys.RETURN)

# 검색 결과 대기
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-title")))

# 첫 번째 검색 결과 저장
  driver.find_element(By.CLASS_NAME, "product-title").text
```

---

### **로그인 상태와 비로그인 상태 검색 결과 비교**
#### **설명**
로그인한 상태와 로그인하지 않은 상태에서 검색 기능을 실행한다.  
검색 결과를 비교하여, **로그인 여부에 따라 검색 결과가 달라지는지 확인**한다.  

#### **구현 방식 및 사용 요소**
```python
# 로그인 상태에서 검색 결과 저장
  first_product_logged_in = driver.find_element(By.CLASS_NAME, "product-title").text

# 비로그인 상태에서 검색 결과 저장
  first_product_logged_out = driver.find_element(By.CLASS_NAME, "product-title").text

# 검색 결과 비교
  assert first_product_logged_in == first_product_logged_out
```

---

✅ **테스트 시나리오를 기반으로 QA 자동화 테스트를 진행할 수 있습니다.** 🚀
