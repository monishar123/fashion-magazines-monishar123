SELECT 
    c.customer_name AS Customer, 
    printf('$%.2f', (s.price_per_month * o.subscription_length)) AS Amount_Due
FROM 
    orders o
JOIN 
    customers c ON o.customer_id = c.customer_id
JOIN 
    subscriptions s ON o.subscription_id = s.subscription_id
WHERE 
    o.order_status = 'unpaid' AND 
    s.description LIKE '%Fashion Magazine%'
GROUP BY 
    c.customer_id;