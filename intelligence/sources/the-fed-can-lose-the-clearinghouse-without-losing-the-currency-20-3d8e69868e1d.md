# The Fed Can Lose the Clearinghouse Without Losing the Currency

**Type:** bridge essay / interpretive synthesis

**Status:** pending workbench synthesis; built on cited factual research;
admitted as an interpretive supporting document under Research Desk object
`fed-clearing-treasury`; not promoted to the vault, Observatory, wrapper, or
installed app

**Evidence cutoff:** public reachability through 2026-08-29

**Companion factual refresh:**
[District Fed Technology and Operating Foundation Refresh](../sources/district-fed-technology-and-operating-foundation-refresh-2026-08--26de24a480da.html)

## The sentence

> **The Fed can lose the clearinghouse without losing the currency.**

That sentence works because the clearinghouse and the currency are not the same
thing.

They have lived close enough together for a century that they can look like one
body. They are not.

The currency is the unit in which the promise is written. The money claim is
the promise itself. The payment rail carries instructions. The clearinghouse
matches, nets, margins, and mutualizes obligations. The settlement asset ends
the obligation. The backstop supplies liquidity when ordinary promises stop
circulating.

The Federal Reserve touches all of those layers. It does not have to own all of
them for the dollar to remain the dollar.

## 1. Unbundle the dollar

The old picture is too simple:

```text
dollar payment -> bank -> Federal Reserve -> final
```

The working picture has more parts:

```text
unit of account:          U.S. dollar
claim presented to user: bank deposit, stablecoin, cash, fund share, other claim
message and transfer:     card, ACH, wire, instant rail, blockchain, shared ledger
clearing and netting:     bank, correspondent, network, CCP, clearinghouse
settlement asset:         reserves, bank money, prefunded private money, securities
safe-asset backing:       reserves, deposits, Treasury bills, repo, other allowed assets
stress backstop:          private liquidity, market sale, bank credit, Fed liquidity
```

Each line can move to a different institution.

That is the change now under way. It is not simply digitization. It is the
separation of functions that the twentieth-century banking bundle held together.

## 2. What it means to lose the clearinghouse

The Fed would “lose the clearinghouse” if a growing share of dollar obligations
were:

- entered on private ledgers;
- matched and netted by private utilities;
- margined by private clearinghouses;
- transferred around the clock without a Fed message crossing the wire for each
  customer transaction; and
- discharged within a private network until a later redemption, rebalance, or
  settlement event touched the banking system.

That loss would be real. The Fed could lose:

- some direct transaction flow;
- fee revenue and customer contact;
- control over the operating clock;
- some admission power at the payment gate;
- some visibility into payment behavior;
- influence over message formats and release cycles; and
- the power that comes from being the unavoidable daily route.

But those losses do not by themselves change the name of the unit. A private
ledger can move a claim denominated in dollars. A clearinghouse can calculate a
dollar obligation. A stablecoin can promise redemption at one dollar. A
Treasury bill can anchor that promise. The transaction can remain dollarized
even when the Fed does not process the user's transfer.

The same pattern is already familiar. Card networks move dollar payments over
private systems. Private clearinghouses net securities and derivatives. The Fed
often appears at a lower settlement layer rather than at the customer-facing
edge.

## 3. Treasury-backed stablecoins make the split visible

The GENIUS Act gives the separation a legal form. It requires permitted payment
stablecoins to maintain identifiable reserves at least one-for-one and allows a
reserve mix that includes money at a Reserve Bank, demand deposits, short-dated
Treasury securities meeting the statute's 93-day test, qualifying repo and
reverse repo, and government money-market funds invested in the allowed assets.

The implementing rules were still proposed at this essay's cutoff, and the Act
had not yet reached its outside effective date. The architecture nevertheless
matters now.

Source: [OCC, proposed GENIUS Act implementing rule](https://occ.gov/news-issuances/federal-register/2026/91fr10202.pdf).

It permits this chain:

```text
user holds a private dollar token
        -> token moves on a private ledger
        -> issuer holds short public debt or other permitted reserves
        -> redemption turns the token back into bank money
        -> stress liquidity comes from asset sales, repo, banks, or ultimately
           the public backstop around the dollar system
```

The Fed is no longer the only route. The state remains inside the asset.

This is why Treasury backing can weaken the Fed's daily routing position while
strengthening the dollar's reach. A person outside the United States may acquire
and transfer a dollar claim without opening a U.S. bank account or sending each
payment through Fedwire. The issuer may answer the new demand by buying short
Treasuries. Private circulation then deepens demand for public dollar assets.

The Jackson Hole paper by Gordon Liao, Eswar Prasad, and Tony Zhang states the
mechanism plainly: dollar-backed stablecoins can make safe dollar claims easier
to acquire, deepen the Treasury market, and reinforce dollar dominance. One
author is affiliated with Circle, so the institutional interest must remain in
view. But the mechanism does not depend on accepting the paper's whole model.

Source: [Liao, Prasad, and Zhang, Financial Innovation and the International Monetary System](https://www.kansascityfed.org/documents/18555/prasad.pdf).

## 4. The central-bank papers are biased—and not simply wrong

Central-bank and central-bank-adjacent papers tend to begin with four values:

1. one money should trade at par;
2. settlement should remain safe under stress;
3. liquidity must be elastic when private balance sheets retreat; and
4. the central bank should be able to see and influence the system it must
   rescue.

That starting point tilts the literature toward central-bank money, regulated
bank deposits, interoperability, and permissioned systems. It can make private
fintech look guilty before trial.

The bias is institutional. It is also rooted in real problems.

Private rails do not repeal:

- runs;
- operational failure;
- maturity and liquidity transformation;
- fragmented pools of collateral;
- loss of netting efficiency;
- unequal redemption paths;
- sanctions and financial-crime controls;
- issuer insolvency;
- cyber risk; or
- the need for someone to provide cash when markets will not.

Darrell Duffie's Jackson Hole paper says systemically important tokenized
markets still need an adequate cash leg. He lays out tokenized reserves,
synchronized conventional reserves, narrow-bank money, and unusually safe
stablecoins as possible designs. Crucially, he also records that the U.S. Fed
has experimented through Projects Cedar and Pine but has **not announced a
tokenized-reserve pilot**.

Source: [Duffie, Tokenized Finance and the Perimeter of Central Banking](https://www.kansascityfed.org/documents/18556/duffie.pdf).

Wenxin Du attacks a different assumption. She argues that 24/7 atomic gross
settlement is not automatically progress because netting and liquidity-saving
mechanisms are economic tools, not old-fashioned clutter. If every obligation
must be funded and settled one by one, the new rail can consume more liquidity
than the old one. Her preferred path is extended RTGS, wider access,
interoperability, resilience, and better existing infrastructure.

Source: [Du, Three Myths About Payment Innovation](https://www.kansascityfed.org/documents/18601/Du_JH_Panel_Remarks_to_Post.pdf).

Christine Parlour, Uday Rajan, and Haoxiang Zhu add a separate warning. Bank
accounts create transaction information that can support credit decisions. A
token network may move the payment while losing that bank-borrower information
channel. That is not proof that private tokens fail; it is a reminder that the
old bundle produced more than settlement.

Source: [Parlour, Rajan, and Zhu, Stablecoin Risk](https://www.kansascityfed.org/documents/18592/parlour.pdf).

## 5. The middle-ground truth

The private-rail story and the central-bank story each overclaim when told
alone.

The strongest middle reading is:

> Private systems can take the transaction route. They cannot make liquidity,
> credit, legal finality, and sovereign trust disappear.

And its mirror is:

> Public backing can anchor the unit. It does not require the central bank to
> own the wallet, the message, the clearinghouse, or every settlement interface.

That is the constitutional opening.

The Fed can retreat from bilateral market privilege. The FOMC can elect to
route some of the Federal Reserve's own otherwise-exempt Treasury and repo
operations through common CCPs. Congress and regulators can permit more private
dollar issuers. The Fed can settle only the net or residual obligation. It can
keep the unit, the reserve asset, the discount window, monetary policy, and the
emergency balance sheet.

This would be a smaller daily Fed and a harder crisis Fed.

The danger is that private actors receive the profitable flow while the public
institution keeps the tail. If private networks clear the easy days but rely on
the Fed when redemptions surge, collateral gaps open, or settlement banks fail,
the Fed may lose ordinary control without losing extraordinary liability.

That is not abolition. It is a new division of labor.

## 6. What the district Banks are building beneath the argument

The technological map of the twelve Reserve Banks is not background. It is the
Fed's institutional answer to this pressure.

The Banks are converting themselves from twelve partly duplicated operating
organizations into specialized nodes of one national machine:

- New York executes market operations and is moving them through FedTrade Plus.
- Richmond hosts National IT and the System CIO under an inter-Bank structure.
- FRFS manages the national payment portfolio under presidents-led enterprise
  governance.
- contractor Banks are meant to lead shared functions for the others.
- a common AI platform and coding tools are already in internal use.
- local independence is being reserved for monetary voice, supervision,
  discount-window work, and regional intelligence.

The Fed is therefore centralizing the inside as the dollar system decentralizes
the outside.

That is not a contradiction. It is survival strategy. A less central external
position makes internal duplication more dangerous. If the Fed's rails must
compete with private instant networks, stablecoins, tokenized deposits, and
shared ledgers, the Fed cannot afford twelve technology stacks and twelve veto
points.

The district Banks do not disappear. Their nature changes. They become:

- local sensing and supervision nodes;
- legal account and credit gates;
- specialized national service contractors;
- hosts of shared infrastructure;
- policy voices inside the FOMC; and
- operating limbs of a common technical constitution.

The center of gravity moves from **Bank ownership of a full stack** to **Bank
participation in a governed network**.

## 7. The Fedwire delay is a small fact with a large meaning

On August 27, the day Jackson Hole opened, FRFS moved its planned November 2026
Fedwire Funds release to November 2027 after Swift delayed its own standards
release. FRFS said it wanted alignment among major market infrastructures and
global interoperability.

Source: [FRFS, Fedwire November release rescheduled](https://www.frbservices.org/news/communications/082726-fedwire-november-release-rescheduled).

Fedwire is operated by the Reserve Banks. Yet its calendar moved because the
network around it moved.

That is the whole essay in miniature.

Sovereign legal control does not mean operational solitude. Even the central
bank's own rail lives inside standards, vendors, bank systems, global messages,
and participant readiness. The Fed can own the wire and still be bound by the
network.

The reverse can also be true. A private stablecoin network can own the customer
route and still be bound by the dollar, Treasury collateral, banking
redemption, and the Fed's stress machinery.

Power sits in the dependencies between layers.

## 8. What “castration” means here

The castration thesis should not mean that the Fed is destroyed or removed.
Removal would be abolition. Castration is retention with particular powers
bound, narrowed, exposed, or transferred to other legal and operating actors.

It means the mixed body is being cut into named powers:

- Congress defines new dollar issuers and reserve assets.
- Treasury debt becomes the backing stock for private money claims.
- private networks move the claims;
- clearinghouses net and mutualize market obligations;
- the Reserve Banks operate shared public rails and account gates;
- the Board writes rules and oversees;
- the FOMC sets the stance and authorizes market operations;
- New York executes those operations; and
- courts and elected branches test the outer limits of independence.

The Fed loses the fog that once let all of those roles appear as one sovereign
thing.

But losing the fog may protect the core. A central bank with fewer daily
privileges can make a stronger claim to independence over the narrow questions
that remain monetary: the unit, the rate, the reserve supply, and emergency
liquidity.

The private-rail transition can therefore do two things at once:

- castrate the Fed as universal gatekeeper; and
- preserve the Fed as final backstop for a wider dollar network.

## 9. When the sentence would stop being true

“The Fed can lose the clearinghouse without losing the currency” is a thesis,
not a law of nature.

It weakens if:

- dollar tokens cease to redeem reliably at par;
- backing migrates away from public dollar assets;
- private ledgers adopt a different unit of account;
- tax, wages, contracts, collateral, and trade invoicing move materially out of
  dollars;
- Treasury markets lose their safe-asset role;
- the Fed cannot supply liquidity to the institutions that connect private
  money to the public anchor; or
- network fragmentation becomes so severe that “one dollar” no longer means
  one interchangeable claim.

It strengthens if:

- stablecoin circulation grows alongside short-Treasury demand;
- private transfers expand while redemptions stay at par;
- clearinghouses and token networks settle only residual positions through
  banks or public money;
- the Fed supplies a narrow reserve and backstop layer without owning the
  customer rail;
- private infrastructures become interoperable with Fedwire, FedNow, or
  reserve-account transfers; and
- the Reserve Banks complete their internal operating constitution while
  remaining legally distinct.

## Closing

The dollar does not belong to one pipe.

It is a unit held together by law, taxation, contract, safe assets, market
depth, convertibility, and the promise of liquidity under stress. The Fed is
the strongest single keeper of that promise. It is not the only machine capable
of moving a dollar claim.

Stablecoins make that distinction hard to ignore. They can take a Treasury bill,
wrap its dollar trust in a private liability, and send the claim across a
private ledger. Clearinghouses can take millions of gross obligations and turn
them into a few net settlement demands. Banks and fintechs can build the user
edge. The Fed can remain underneath rather than in front.

So the real question is not whether the Fed wins or fintech wins.

It is:

> Who owns the route, who carries the risk, who supplies the safe asset, and who
> must still answer when the route breaks?

The likely answer is not one institution.

The Fed can lose the clearinghouse without losing the currency. It may even
lose the clearinghouse **because** private rails make the currency travel
farther.

The price is that the Fed's power becomes narrower, more legible, and more
concentrated at the moment of stress.
