"""SUPPORT D'ATELIER — requête volontairement dangereuse. NE PAS RÉUTILISER. Identifiants fictifs."""

DSN = "postgres://admin:N0valine2026@db-prod.novaline.local/meetroom"  # fictif


def reservations_par_salarie(conn, debut: str, service: str):
    query = (
        "SELECT e.name, e.email, e.dept, COUNT(*) AS nb FROM bookings b "
        "JOIN employees e ON e.id = b.employee_id "
        "WHERE b.start_at >= '" + debut + "' AND e.dept = '" + service + "' "
        "GROUP BY e.id ORDER BY nb DESC"
    )
    return conn.execute(query).fetchall()
