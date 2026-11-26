# Pas en Python ? Les équivalents

MeetRoom est en Python pour rester lisible par tous. Chaque pratique de la formation a son équivalent direct.

| Pratique | Python (MeetRoom) | Java | JavaScript / TypeScript | C# / .NET |
|---|---|---|---|---|
| Tests | pytest | JUnit | Jest, Vitest | xUnit, NUnit |
| Analyse statique | ruff, bandit | SpotBugs, SonarQube | ESLint, SonarQube | Analyseurs Roslyn |
| Audit des dépendances | pip-audit | OWASP Dependency-Check | `npm audit` | `dotnet list package --vulnerable` |
| Données synthétiques | Faker | Datafaker | @faker-js/faker | Bogus |
| Scan de secrets | gitleaks | gitleaks | gitleaks | gitleaks |
| Verrouillage des versions | `requirements.txt` avec empreintes | `pom.xml` / `gradle.lockfile` | `package-lock.json` | `packages.lock.json` |

## La requête paramétrée, dans chaque langage
Le principe est toujours le même : la valeur voyage **à côté** de la requête, jamais dedans.

```python
# Python
db.execute("SELECT * FROM bookings WHERE ref = :ref", {"ref": ref})
```
```java
// Java (JDBC)
PreparedStatement ps = conn.prepareStatement("SELECT * FROM bookings WHERE ref = ?");
ps.setString(1, ref);
```
```javascript
// JavaScript (node-postgres)
await client.query("SELECT * FROM bookings WHERE ref = $1", [ref]);
```
```csharp
// C# (ADO.NET)
var cmd = new SqlCommand("SELECT * FROM bookings WHERE ref = @ref", conn);
cmd.Parameters.AddWithValue("@ref", reference);
```

## Ce qui ne change pas d'un langage à l'autre
`AGENTS.md`, les permissions de l'agent, le hook de garde, le scan de secrets, le modèle de pull request,
la charte, et surtout la relecture humaine.

## Exercice
Demandez à votre assistant : « Traduis `app/repository.py` dans mon langage, avec les mêmes garanties
(requêtes paramétrées, typage). » Puis relisez le résultat avec la checklist de la partie 2 :
c'est un excellent test de votre capacité à relire du code généré.
