-- 1.List the following details of each employee: 
-- employee number, last name, first name, gender, and salary.
SELECT e.last_name, e.first_name, e.gender, s.salary
FROM salaries AS s
INNER JOIN employees AS e ON
e.emp_no=s.emp_no;

-- 2. List employees who were hired in 1986.
SELECT emp_no, last_name, first_name, hire_date 
FROM employees
WHERE hire_date >= '1986-01-01' AND hire_date <= '1986-12-31';

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, 
-- last name, first name, and start and end employment dates.
SELECT m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name, m.from_date, m.to_date 
	FROM dept_manager AS m
	INNER JOIN employees AS e ON m.emp_no=e.emp_no
	LEFT JOIN departments AS d ON m.dept_no=d.dept_no;
	
-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM dept_emp AS m
	INNER JOIN employees AS e ON m.emp_no=e.emp_no
	LEFT JOIN departments AS d ON m.dept_no=d.dept_no;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT emp_no, last_name, first_name
FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%'
ORDER BY last_name;

-- 6. List all employees in the Sales department, 
-- including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM dept_emp AS m
	INNER JOIN employees AS e ON m.emp_no=e.emp_no
	LEFT JOIN departments AS d ON m.dept_no=d.dept_no
	WHERE d.dept_name='Sales';

-- 7. List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM dept_emp AS m
	INNER JOIN employees AS e ON m.emp_no=e.emp_no
	LEFT JOIN departments AS d ON m.dept_no=d.dept_no
	WHERE d.dept_name='Sales' OR d.dept_name='Development';

-- 8. In descending order, list the frequency count of employee last names, 
-- i.e., how many employees share each last name.
SELECT last_name, COUNT(*) AS frequency
FROM employees
GROUP BY last_name
ORDER BY COUNT(*) DESC;



