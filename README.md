# Coding Test

Hi Thomas Bourton!

Software engineering is at the heart of what we do here at giffgaff. Our agile engineering teams build and support a wide variety of applications and services. These combine to create our unique user experience on the giffgaff website, enable a whole range of awesome features via modern APIs and, additionally, enable our internal teams to work in the most productive and efficient ways.

The quality and maintainability of our software is very important to us, so we are looking for engineers with real-world experience of building and running contemporary software, especially in terms of the whole development lifecycle. You will help us to design and implement tightly focussed APIs, user interfaces, services that internalise our core business logic or internal tools and, together with your team, you will support them in production. We want you to share your opinions on how we are doing things - and help us get better!

## Have you got what it takes?

<details>
  <summary>Basic Expectations</summary>
  <br/>
  <ul>
    <li>Love delivering a wow to our members</li>
    <li>Ability to communicate clearly</li>
    <li>Be curious & creative</li>
    <li>Have excellent attention to detail</li>
    <li>Have an interest in technology, mobile and wider popular culture trends</li>
    <li>Able to work under pressure and manage workloads effectively</li>
    <li>Organised, self motivated and accountable for own workload</li>
    <li>A strong team player</li>
  </ul>
  <br/>
</details>
<details>
  <summary>Key Attributes & Behaviours</summary>
  <br/>
  <strong>Community & Connectedness</strong>
  <p>A person with community & connectedness skills has a sense of being part of a larger whole, a desire to contribute, a sense that the other people (i.e. coworkers, users, members) are not simply characters in his or her own movie, but fully-realised individuals.</p>
  <ul>
    <li>Coach & Mentor</li>
    <li>Courageous & Honest</li>
    <li>Code with Empathy</li>
    <li>Open Source Approach</li>
  </ul>
  <br/>
  <strong>Leadership</strong>
  <p>A person with leadership skills knows how to develop and follow a sense of purpose, in themselves and in others. They are willing to point out, own, and fix things that are broken about our company and in their own career tracks.</p>
  <ul>
    <li>An Owner’s Mindset</li>
    <li>Good at Persuasion</li>
    <li>A Sense of Purpose</li>
    <li>Do the Next Right-Thing</li>
  </ul>
  <br/>
  <strong>Technical Capability</strong>
  <p>A person with high technical capability is technically curious, tackles problems without giving up, and produces solutions that less-experienced folks can use, maintain, and learn from.</p>
  <ul>
    <li>Creative & Curious</li>
    <li>Disciplined & Rigorous</li>
    <li>Fearless & Pragmatic</li>
    <li>Good at Problem Solving</li>
    <li>A Propensity to Ship</li>
  </ul>
  <br/>
</details>
<details>
  <summary>Core Engineering Skills</summary>
  <br/>
  <table>
    <tr><td rowspan="4" valign="top">Must Have</td><td>Reading & Writing Code</td></tr>
    <tr><td>Variables & Control Structures</td></tr>
    <tr><td>Debugging & Troubleshooting</td></tr>
    <tr><td>IDE & OS Basics</td></tr>
    <tr><td rowspan="4" valign="top">Should Have</td><td>Test Driven Development</td></tr>
    <tr><td>Pair Programming</td></tr>
    <tr><td>Clean Code & Refactoring</td></tr>
    <tr><td>Version Control</td></tr>
    <tr><td rowspan="6" valign="top">Could Have</td><td>Continuous Integration & Deployment</td></tr>
    <tr><td>Algorithms & Data Structures</td></tr>
    <tr><td>Dependency Injection</td></tr>
    <tr><td>Mocks & Stubs</td></tr>
    <tr><td>Alerting & Monitoring</td></tr>
    <tr><td>Functional & Non-Functional Testing</td></tr>
    <tr><td rowspan="4" valign="top">Would Like</td><td>SOLID Principles</td></tr>
    <tr><td>Containerisation & Networking Basics</td></tr>
    <tr><td>Twelve Factor App Design</td></tr>
    <tr><td>Solution Architecture</td></tr>
  </table>
</details>
<details>
  <summary>Our Technology Stack</summary>
  <br/>
  <table>
    <tr><td rowspan="8" valign="top">Client-Side</td><td>CSS3</td></tr>
    <tr><td>ECMAScript (ES6+)</td></tr>
    <tr><td>HTML5</td></tr>
    <tr><td>Jest</td></tr>
    <tr><td>React</td></tr>
    <tr><td>React Native</td></tr>
    <tr><td>SASS</td></tr>
    <tr><td>TypeScript</td></tr>
    <tr><td rowspan="6" valign="top">Server-Side</td><td>Java 8 with Maven</td></tr>
    <tr><td>JUnit</td></tr>
    <tr><td>Node JS</td></tr>
    <tr><td>PHP & Laravel</td></tr>
    <tr><td>Python</td></tr>
    <tr><td>Spring Framework</td></tr>
    <tr><td rowspan="8" valign="top">Additional</td><td>Apache & NGINX</td></tr>
    <tr><td>AWS</td></tr>
    <tr><td>Jenkins</td></tr>
    <tr><td>DynamoDB, PostgreSQL, Redis & Oracle</td></tr>
    <tr><td>Docker & Kubernetes</td></tr>
    <tr><td>ElasticSearch & Kibana</td></tr>
    <tr><td>Grafana & Prometheus</td></tr>
    <tr><td>Kinesis</td></tr>
  </table>
</details>

## The Challenge

We would like you to complete the following coding exercise.

You can use any programming language you like. Ideally your solution will include unit tests, preferably written using a [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) approach. The code related to your solution should be placed in a subfolder and be easy to execute - ideally **clone** → **install** → **run**

Please commit your code back to this repository frequently. We expect you to complete this exercise within a day, but if takes a little longer don't worry - just let us know when you're done.

> NOTE: Due to 2FA if you're using HTTPS to access this repo, you must create a personal access token to use as a password when [authenticating to GitHub on the command line using HTTPS](https://help.github.com/en/github/authenticating-to-github/accessing-github-using-two-factor-authentication#authenticating-on-the-command-line-using-https) URLs.


---

<details>
<summary>Exercise 1 (Recommended: 1 Hour)</summary>

---

## Single Poker Hand Ranking Service

### Requirements:

You have to implement a poker hand ranking service:
- Write an algorithm that takes a hand of cards and identifies the ranking of the given hand.
- Expose an API to serve this algorithm via an endpoint `/rank`, that accepts a valid poker hand and returns its ranking.
- Rank information should be formatted as `<rank_name>: <description>`, see description format for each different rank below.
<br>

### Rules:

A poker hand consists of 5 cards dealt from a deck. A deck is composed of 52 cards ordered as `2 through 10`, `J` (*Jack*), `Q` (*Queen*), `K` (*King*), and `A` (*Ace*); and split across 4 suits: *♠ Spades* (black), *♦ Diamonds* (red), *♣ Clubs* (black), and *♥ Hearts* (red).

Poker hands are ranked by the following partial order from highest to lowest:

**1. Royal Flush**  ~ `[ A♥ K♥ Q♥ J♥ 10♥ ]`

The best hand possible, a royal flush consists of A, K, Q, J and 10, all of the same suit.

Description format: `<suit>`

**2. Straight Flush** ~ `[ 6♥ 7♥ 8♥ 9♥ 10♥ ]`

Also very rare, a straight flush consists of any straight that is all the same suit. Note Ace can act as value `1` to form a straight with values `2 3 4 5`.

Description format: `<highest_value>-high <suit>`

**3. Four of a Kind** ~ `[ A♥ A♣ A♦ A♠ K♥ ]`

Four of a kind, or 'quads', consists of four cards of equal value along with another card known as a side card.

Description format: `<quads value>`

**4. Full House** ~ `[ A♥ A♣ A♦ K♠ K♥ ]`

A full house consists of three cards of one value and two cards of another.

Description format: `<trips_value> over <pair_value>`

**5. FLush** ~ `[ K♣ 10♣ 8♣ 7♣ 5♣ ]`

A flush is a hand which has all cards of the same suit.

Description format: `<suit>`

**6. Straight** ~ `[ 10♥ 9♣ 8♦ 7♠ 6♥ ]`

A straight has five cards of consecutive value that are not all the same suit. Note Ace can act as value `1` to form a straight with values `2 3 4 5`.

Description format: `<highest_value>-high`

**7. Three of a Kind** ~ `[ A♥ A♣ A♦ K♠ Q♥ ]`

Also known as 'trips', three of a kind is 3 cards of the same value and 2 side cards of different values.

Description format: `<trips value>`

**8. Two Pair** ~ `[ A♥ A♣ K♦ K♠ 7♥ ]`

Two pair cosists of two sets of cards of the same value, and one extra card.

Description format: `<high_pair_value> and <low_pair_value>`

**9. Pair** ~ `[ A♥ A♣ K♦ J♠ 7♥ ]`

One pair consists of two cards of the same value, and three extra cards.

Description format: `<pair_value>`

**10. High Card** ~ `[ A♥ K♣ Q♦ 9♠ 7♥ ]`

Five cards that do not interact with each other to make any of the above hands.

Description format: `<value>`

<br>

### Samples:

```
Query: "2H 3D 5S 9C KD"
Result: "high card: King"

~

Query: "2H 4D 4S 2C 4H"
Result: "full house: 4 over 2"

~

Query: "6H 7H 8H 9H 10H"
Result: "straight flush: 10-high hearts"
```

</details>

---


Good Luck!

#### Generated for [TBourton](https://github.com/TBourton) on Wed Feb 15 2023 10:04:16 GMT+0000 (Coordinated Universal Time)
